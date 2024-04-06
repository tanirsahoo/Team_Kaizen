import os
import subprocess
import stat

def list_shell_scripts(directory):
    """ List all shell script files in the specified directory. """
    shell_scripts = []
    for filename in os.listdir(directory):
        if filename.endswith(".sh"):
            shell_scripts.append(filename)
    return shell_scripts

def select_script(shell_scripts):
    #""" Display a list of shell scripts and prompt user to select one. """
    #print("Available Shell Scripts:")
    #for index, script in enumerate(shell_scripts, start=1):
        #print(f"{index}. {script}")
    #try:
        #choice = int(input("Enter the number of the script to execute (or 0 to exit): "))
        #if choice == 0:
            #return None
        #elif 1 <= choice <= len(shell_scripts):
            #return shell_scripts[choice - 1]
        #else:
            #print("Invalid choice. Please try again.")
            #return select_script(shell_scripts)
    #except ValueError:
        #print("Invalid input. Please enter a number.")
        #return select_script(shell_scripts)
    """ Display a list of shell scripts and prompt user to select one. """
    print("Available Shell Scripts:")
    for index, script in enumerate(shell_scripts, start=1):
        print(f"{index}. {script}")
    array_of_index = []
    try:
        hard_scripts = input("Enter the index of files you want to execute.")
        character_list = hard_scripts.split(',')
        j = 0
        for items in character_list:
            array_of_index.append(shell_scripts[int(items)])
            print(array_of_index[j])
            j = j + 1
        return array_of_index
    except ValueError:
        print("Invalid input. Please enter a number.")
        #return array_of_index
        return select_script(shell_scripts)
    

def execute_script(script , script_directory):
    """ Execute the selected shell script. """
    try:
        for items in script:
            script_path = os.path.join(script_directory, items)
            subprocess.run(["bash", script_path])
    except Exception as e:
        print("There is some exception")
    
def change_permissions_recursive(directory):
    print("Inside the permission change function")
    """ Recursively traverse the directory and change permissions of shell script files. """
    for root, dirs, files in os.walk(directory):
        print("Inside the permission change function")
        for filename in files:            
            if filename.endswith(".sh"):                
                script_path = os.path.join(root, filename)                
                # Get current file permissions
                current_permissions = os.stat(script_path).st_mode
                # Add execute permission if it's not already set
                if not (current_permissions & stat.S_IXUSR):
                    new_permissions = current_permissions | stat.S_IXUSR
                    os.chmod(script_path, new_permissions)
                    print(f"Changed permissions for: {script_path}")
                    
                    
def main():
    # Directory containing your shell scripts
    script_directory = "/home/tanir/Smart_India_Hackathon/Team_Kaizen/Hardening_Script_Files/Hard Scripts"
    
    #Change the permission of shell files.
    change_permissions_recursive(script_directory)

    # List all shell scripts in the directory
    scripts = list_shell_scripts(script_directory)

    if not scripts:
        print("No shell scripts found in the specified directory.")
    else:
        # Allow user to select and execute a script
        selected_script = select_script(scripts)
        if selected_script:
            execute_script(selected_script , script_directory)
            print(f"Script '{selected_script}' executed.")
        else:
            print("Exiting script execution.")

if __name__ == "__main__":
    main()

