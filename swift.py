# -*- coding: utf-8 -*-
import idaapi
import idc
import idautils
import subprocess


class Swift_Dump_t(idaapi.plugin_t):
    comment = "Swift Dump plugin for IDA Pro 7.0"
    help = "https://github.com/paradiseduo/ida-swift-demangle/issues"
    wanted_name = "Swift Dump"
    wanted_hotkey = "Ctrl-Alt-D"
    flags = idaapi.PLUGIN_KEEP

    def init(self):
        return idaapi.PLUGIN_OK

    def term(self):
        return idaapi.PLUGIN_OK

    def patcher(self):
        AllFunc = []
        AllFuncName = []
        for func in idautils.Functions():
            name = GetFunctionName(func)
            AllFunc += [func]
            if name[:1] == "_":
                name = name[1:]
            AllFuncName += [name]

        proc = subprocess.Popen('xcrun swift-demangle --simplified --compact', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        proc.stdin.write('\n'.join(AllFuncName))
        proc.stdin.close()
        results = proc.stdout.read().split('\n')
        proc.wait()
        i = 0
        for addr in AllFunc:
            old_name = AllFuncName[i]
            new_name = results[i]
            if new_name != old_name:
                MakeNameEx(addr, new_name, SN_NOCHECK|SN_NOWARN)
                SetFunctionCmt(addr, "%s \n%s" % (old_name, new_name), 1)
            i += 1

    def run(self, arg):
        self.patcher()


# register IDA plugin
def PLUGIN_ENTRY():
    return Swift_Dump_t()
