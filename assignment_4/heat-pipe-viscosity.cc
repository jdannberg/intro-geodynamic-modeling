#include <aspect/geometry_model/interface.h>
#include <aspect/material_model/visco_plastic.h>
#include <aspect/simulator_access.h>

namespace aspect
{
  namespace MaterialModel
  {
    using namespace dealii;

    template <int dim>
    class HeatPipeViscosity : public MaterialModel::ViscoPlastic<dim>
    {
      public:

        virtual void evaluate(const MaterialModel::MaterialModelInputs<dim> &in,
                              MaterialModel::MaterialModelOutputs<dim> &out) const;
    };

  }
}

namespace aspect
{
  namespace MaterialModel
  {

    template <int dim>
    void
    HeatPipeViscosity<dim>::
    evaluate(const MaterialModel::MaterialModelInputs<dim> &in,
             MaterialModel::MaterialModelOutputs<dim> &out) const
    {
      ViscoPlastic<dim>::evaluate(in, out);
      for (unsigned int i=0; i < in.position.size(); ++i)
        {
          const double depth = this->get_geometry_model().depth(in.position[i]);
          const double solidus = 1100.0 + 400.0 * depth/100000.0;
          if(in.temperature[i] > solidus)
            out.viscosities[i] *= std::exp(0.005*(solidus - in.temperature[i]));
          out.viscosities[i] = std::min(out.viscosities[i],1.e25 / (1.e7 * (0.5+0.5*tanh((5000.0-depth)/1000.0))+1.0));
          out.viscosities[i] = std::max(out.viscosities[i], 1.e16);
        }
    }
  }
}

// explicit instantiations
namespace aspect
{
  namespace MaterialModel
  {
    ASPECT_REGISTER_MATERIAL_MODEL(HeatPipeViscosity,
                                   "heat pipe viscosity",
                                   "no description.")
  }
}
