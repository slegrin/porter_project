from os.path import join, realpath
from datetime import datetime
Import("env")

def after_build(source, target, env):
    # Get the current date and time
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Define the new binary path with the desired pattern
    bin_path = join(env.subst("$BUILD_DIR"), f"porter_{current_time}_firmware.bin")
    
    # Convert the target to string to get the firmware path
    firmware_path = str(target[0])
    
    # Execute the objcopy command to generate the binary
    env.Execute(" ".join(["arm-none-eabi-objcopy", "-O", "binary", firmware_path, bin_path]))
    
    # Print the path of the saved binary
    print("Firmware binary saved at: {}".format(realpath(bin_path)))

# Add post-action to the build process
env.AddPostAction("buildprog", after_build)
