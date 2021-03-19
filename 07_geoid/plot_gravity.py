# This model computes the gravity anomaly
# of a layer of dense material.

set Dimension = 3
set CFL number                             = 0.1
set End time                               = 0
set Output directory                       = output
set Resume computation                     = false
set Start time                             = 0
set Adiabatic surface temperature          = 1600
set Surface pressure                       = 0
set Pressure normalization                 = no
set Timing output frequency                = 5
set Use years in output instead of seconds = true
set Nonlinear solver scheme                = no Advection, no Stokes


subsection Discretization
  set Stokes velocity polynomial degree       = 2
  set Temperature polynomial degree           = 2
  set Use locally conservative discretization = false
  subsection Stabilization parameters
    set alpha = 2
    set beta  = 0.078
    set cR    = 0.5   # default: 0.11
  end
end


subsection Geometry model
  set Model name = chunk
  subsection Chunk
    set Chunk minimum longitude = 160
    set Chunk maximum longitude = 200
    set Chunk minimum latitude = -20
    set Chunk maximum latitude = 20
    set Longitude repetitions = 10
    set Latitude repetitions = 10
    set Chunk inner radius = 6071000
    set Chunk outer radius = 6371000
    set Radius repetitions = 1
  end
end


subsection Gravity model
  set Model name = ascii data
end


subsection Initial temperature model
  set List of model names = function #adiabatic, function
  subsection Function 
    set Coordinate system = spherical
    set Variable names      = r, phi, theta
    set Function constants  = d=0.1, angle=89
    set Function expression =  if( sqrt( (phi-3.1416)^2 + (theta-1.57079632679)^2 + ((r-6221000)/4e6)^2) < 0.05, 800, 1000.0) \
                             + if( sqrt( (phi-3.1416-d)^2 + (theta-1.57079632679)^2 + ((r-6221000)/4e6)^2) < 0.05, -150, 0)
    set Function expression =  if( sqrt( (tan(angle/180*3.1416)*(phi-3.0)+(r-6371000)/4e6)^2) < 0.03*tan(angle/180*3.1416) && sqrt((theta-1.57079632679)^2) < 0.2, 800, 1000.0) 
  end

  subsection Adiabatic
    set Age top boundary layer = 1e8
  end
end


subsection Material model
  set Model name = simple
  subsection Simple model
    set Reference density             = 1000
    set Reference specific heat       = 1250
    set Reference temperature         = 0.0
    set Thermal conductivity          = 4.7
    set Thermal expansion coefficient = 1e-3
    set Viscosity                     = 1.e21
  end
end


subsection Mesh refinement
  set Initial adaptive refinement        = 1
  set Initial global refinement          = 1                      # default: 2
  set Refinement fraction                = 0.99
  set Coarsening fraction                = 0.00
  set Strategy                           = temperature
  set Time steps between mesh refinement = 0
end


# The parameters below this comment were created by the update script
# as replacement for the old 'Model settings' subsection. They can be
# safely merged with any existing subsections with the same name.

subsection Boundary temperature model
  set Fixed temperature boundary indicators   = inner, outer
  set List of model names = initial temperature
end

subsection Boundary velocity model
  set Zero velocity boundary indicators       = inner, east, west
end

subsection Mesh deformation
  set Mesh deformation boundary indicators = outer: free surface
  subsection Free surface
    set Free surface stabilization theta = 0.5
  end
end

subsection Termination criteria
  set Termination criteria = end step
  set End step = 10
end

subsection Postprocess
  set List of postprocessors = topography,velocity statistics,visualization, gravity calculation

  subsection Gravity calculation
    set Sampling scheme               = map
    set Number points longitude       = 60
    set Number points latitude        = 60
    set Minimum radius = 6371000
    set Maximum radius = 6371000
    set Minimum longitude = -20
    set Minimum latitude = -20
    set Maximum longitude = 20
    set Maximum latitude = 20
  end

  subsection Visualization
    set List of output variables = material properties, strain rate, nonadiabatic pressure

    subsection Material properties
      set List of material properties = density, viscosity
    end

    set Time between graphical output = 0
    set Interpolate output = true
  end
end

subsection Formulation
  set Formulation = Boussinesq approximation
end
