
# Clock Module

The idea behind this project is to have a standalone clock circuit to debug ICs at a very low clock speed.

It is mainly inspired by [Ben Eater's](https://eater.net/8bit/clock) version.




### Note
This projects was made using the nightly build of KiCad.

**Version: (6.99.0-1487-g4c225cff5b), release build**

 
### Features
- Manual pulse Mode.
- Variable frequency clock.
- DC Input Jack 7v - 15v @ approx. 100mA.
- Raw 5v power in for breadboard compatability.
- Lots of LEDs :)


### Parts
- 2x 0.01uF - Ceramic Capacitor
- 2x 4.7uF - Capacitor
- 1x 470uF - Capacitor
- 1x .33uF - Ceramic Capacitor
- 4x .1uF - Ceramic Capacitor
- 1x 1uF - Capacitor
- 1x 1N4007 - Diode
- 4x 5mm LED
- 2x 01x02 Female Pin header
- 1x DC Jack
- 6x 1K - Resistor
- 2x 51K - Resistor
- 2x 10K - Resistor
- 1x 100K - Potentiometer linear
- 2x Button
- 3x NE555P
- 1x L7805
- 1x 7400



### What does it look like
#### KiCad Render
![alt text](https://raw.githubusercontent.com/JopjeKnopje/clockmodule/main/pics/rev-0-1.png?raw=true)


### Todo
- [ ] Use CMOS ICs for a 5vpp output
- [x] Add partslist
- [ ] Add photos
- [ ] Swap silkscreen position of c3 and c4 
- [ ] Different footprint for c8
- [ ] Remove jclpcb mark

