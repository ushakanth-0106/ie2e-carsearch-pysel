import re, os

dirpath = os.path.dirname(__file__).replace("lib", "data")

def read_file(filename):
    full_path = os.path.join(dirpath, filename)
    with open(full_path, "r") as f:
        return f.read()

def write_file(filename, content):
    full_path = os.path.join(dirpath, filename)
    with open(full_path, "r") as fr:
        op_lines = fr.readlines()
        format_op_lines = [re.compile(r"\n").sub("", z) for z in op_lines]
        format_op_lines.pop(0)
    with open(filename, "w") as fw:
        fw.writelines("\nGiven output file content for Vehicle Details \n")
        [fw.writelines(y + "\n") for y in format_op_lines]
        fw.writelines("\nObtained Vehicle Details from website \n")
        [fw.writelines(x + "\n") for x in content]
        fw.writelines("\nComparision differences \n")
        fw.writelines(set(content) ^ set(format_op_lines))

def get_reg_number(ip_lines):
    pattern = r"\b[A-Z]{2}[0-9]{2} [A-Z]{3}\b"        
    regis = re.findall(pattern, "".join(ip_lines))
    pattern = pattern.replace(" ", "")
    regis_final = regis + re.findall(pattern, "".join(ip_lines))
    return regis_final
