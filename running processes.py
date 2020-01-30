import globalPluginHandler
import ui
import subprocess

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    def get_list_of_console_processes(self):
        call = 'TASKLIST', '/FO', 'CSV'
        output = subprocess.check_output(call)
        output = output.replace(b'"', b'').split(b'\r\n')
        keys = output[0].split(b',')
        proc_list = [i.split(b',') for i in output[1:] if i]
        console_list = []
        for app in proc_list:
            if b"Console" in app[2]:
                if any(app[0].decode("utf-8") in sublist for sublist in console_list) == False: 
                    try:
                        memory_usage = app[4].decode("utf-8")
                        memory_usage = int(memory_usage)
                    except:
                        memory_usage = memory_usage.split(" ")[0]
                        memory_usage = int(memory_usage)
                    console_list.append([app[0].decode("utf-8"), memory_usage])

        return console_list

    def script_topFive(self, gesture):
        
        processes = self.get_list_of_console_processes()
        processes.sort(key = lambda x: x[1], reverse=True)
        message = ""
        for process in processes[0:5]:
            message += process[0] + ", "

        ui.message("The 5 processes with the highest memory usage are: " + message)

    def script_allProcesses(self, gesture):

        processes = self.get_list_of_console_processes()
        message = ""
        for process in processes:
            message += process[0] + ", "

        ui.message("All running processes: " + message)


    def script_runningPrograms(self, gesture):
        call = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
        output = subprocess.check_output(call)
        output = output.split(b"\r\n")
        appList = []
        for app in output[3:]:
            appList.append(app.decode("utf-8").strip())
        
        message = ""
        for app in appList:
            if app != "":
                message += app + ", "
                
        ui.message("All running programs: " + message)


    __gestures={
        "kb:control+NVDA+1":"topFive",
        "kb:Control+NVDA+2":"allProcesses",
        "kb:Control+NVDA+3":"runningPrograms"
    }