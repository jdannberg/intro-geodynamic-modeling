set terminal pngcairo enhanced font "arial,25" fontscale 1.0 size 1200, 800 
set output 'plate.png'

set rmargin 7
set xlabel "Time in years"
set ylabel "Velocity in m/yr"

plot 'output-plate/statistics' using 2:($35-$36) with lines lw 5 lt rgb "dark-blue" title 'velocity difference'
