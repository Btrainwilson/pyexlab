
def get_info(object):
    model_info_op = getattr(object, "info", None)

    if callable(model_info_op):
        return object.info()
    else:
        return "No object.info() function provided"

def dict_str_output(output):

    out_str = ""
    for key in output:
        out_str += "%s : %s\n" %(key, output[key])

    return out_str