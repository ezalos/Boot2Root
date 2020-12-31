# live init

 0. When starting the VM we want to maintain `Shift`:
  ![Step 0](assets/live_init_0.png)
 1. We arrive to this prompt, which is the boot menu:
  ![Step 1](assets/live_init_1.png)
 2. Pressing `Tab` gets us our different booting options:
  ![Step 2](assets/live_init_2.png)
 3. We choose live, but we give the instruction to change init destination to `/bin/bash` so we have access to root shell:
  ![Step 3](assets/live_init_3.png)
 4. We can now verify our level of privileges wit `id`, we are root:
  ![Step 4](assets/live_init_4.png)
