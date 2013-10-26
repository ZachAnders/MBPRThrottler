##MBPR Throttle

My Macbook Pro Retina's GPU begins throttling at around 85C. This would not be so problematic if
throttling did not cause such EXTREME microstuttering. So I wrote a little script that attempts to
listen for the GPU clock speed to 'bounce'. If it does more than like twice, it will repeatedly drop
the clock speed until the stuttering stops. If the stuttering has been absent for like an hour,
it will gradually begin to increase clock speeds.

Clock and memory speeds both have an upper and a lower bound.

Requirements - These files need to be in the same folder:
 - GPU-Z.exe: Can access current GPU clock via shared memory
 - nvidiaInspector.exe - Can set clocks to arbitrary values.
 
It functions decently well, but probably isn't nearly polished enough to be of any use to anyone.
