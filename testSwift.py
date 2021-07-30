import idaapi
import idc
import idautils
import subprocess

class Swift_Dump_t(idaapi.plugin_t):
    comment = "Swift Dump plugin for IDA Pro 7.0"
    help = ""
    wanted_name = "Swift Dump"
    wanted_hotkey = "Ctrl-Alt-D"
    flags = idaapi.PLUGIN_KEEP

    def init(self):
        return idaapi.PLUGIN_OK

    def term(self):
        return idaapi.PLUGIN_OK

    def patcher(self):
        for func in idautils.Functions():
            oldname = GetFunctionName(func)
            if oldname[:2] == "_$":
                oldname = oldname[2:]
                p = subprocess.Popen('xcrun swift-demangle --simplified --compact '+oldname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                newname = str(p.communicate()[0].decode('utf-8', 'ignore').strip())
                if newname != oldname and len(newname) > 2:
                    MakeNameEx(func, newname, SN_NOCHECK|SN_NOWARN)
                    SetFunctionCmt(func, "%s \n%s" % (oldname, newname), 1)

    def run(self, arg):
        self.patcher()


# register IDA plugin
def PLUGIN_ENTRY():
    return Swift_Dump_t()
