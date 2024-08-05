import pickle
import subprocess

def unsafe_deserialization(data):
    return pickle.loads(data)

def command_injection(user_input):
    subprocess.call("echo " + user_input, shell=True)

password = "hardcoded_password"

def get_password():
    return password