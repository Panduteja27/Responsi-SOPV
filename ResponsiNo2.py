import helper

helper.header("Responsi SOP NOMOR 2")

class RoundRobin:

    def ProsesData(self, no_of_processes):
        proses = []
        for i in range(no_of_processes):
            tenggat = []
            prosesKe = str(input("Masukan Nama Aplikasi : "))
            burstTime = int(input(f"Masukan Burst Time Untuk Memproses {prosesKe}: "))
            tenggat.extend([prosesKe, 0, burstTime, 0, burstTime])

            proses.append(tenggat)
        quantumTime = int(input("Masukan Quantum Time : "))
        RoundRobin.schedulingProcess(self, proses, quantumTime)

    def schedulingProcess(self, proses, quantumTime):
        Mulai = []
        selesai = []
        ekseskusiProses = []
        urutan = []
        s_time = 0
        while 1:
            temp = []
            for i in range(len(proses)):
                if proses[i][1] <= s_time and proses[i][3] == 0:
                    present = 0
                    if len(urutan) != 0:
                        for k in range(len(urutan)):
                            if proses[i][0] == urutan[k][0]:
                                present = 1

                    if present == 0:
                        temp.extend([proses[i][0], proses[i][1], proses[i][2], proses[i][4]])
                        urutan.append(temp)
                        temp = []

                    if len(urutan) != 0 and len(ekseskusiProses) != 0:
                        for k in range(len(urutan)):
                            if urutan[k][0] == ekseskusiProses[len(ekseskusiProses) - 1]:
                                urutan.insert((len(urutan) - 1), urutan.pop(k))

            if len(urutan) == 0:
                break
            if len(urutan) != 0:
                if urutan[0][2] > quantumTime:

                    Mulai.append(s_time)
                    s_time = s_time + quantumTime
                    e_time = s_time
                    selesai.append(e_time)
                    ekseskusiProses.append(urutan[0][0])
                    for j in range(len(proses)):
                        if proses[j][0] == urutan[0][0]:
                            break
                    proses[j][2] = proses[j][2] - quantumTime
                    urutan.pop(0)
                elif urutan[0][2] <= quantumTime:

                    Mulai.append(s_time)
                    s_time = s_time + urutan[0][2]
                    e_time = s_time
                    selesai.append(e_time)
                    ekseskusiProses.append(urutan[0][0])
                    for j in range(len(proses)):
                        if proses[j][0] == urutan[0][0]:
                            break
                    proses[j][2] = 0
                    proses[j][3] = 1
                    proses[j].append(e_time)
                    urutan.pop(0)
        t_time = RoundRobin.calculateTurnaroundTime(self, proses)
        w_time = RoundRobin.calculateWaitingTime(self, proses)
        RoundRobin.printData(self, proses, t_time, w_time, ekseskusiProses)

    def calculateTurnaroundTime(self, proses):
        total_turnaround_time = 0
        for i in range(len(proses)):
            turnaround_time = proses[i][5] - proses[i][1]

            total_turnaround_time = total_turnaround_time + turnaround_time
            proses[i].append(turnaround_time)
        rataaanTurnTime = total_turnaround_time / len(proses)

        return rataaanTurnTime

    def calculateWaitingTime(self, proses):
        total_waiting_time = 0
        for i in range(len(proses)):
            waiting_time = proses[i][6] - proses[i][4]

            total_waiting_time = total_waiting_time + waiting_time
            proses[i].append(waiting_time)
        rataanWaitTime = total_waiting_time / len(proses)

        return rataanWaitTime

    def printData(self, proses, rataaanTurnTime, rataanWaitTime, ekseskusiProses):
        proses.sort(key=lambda x: x[0])
  
        print(
            "prosesKe  Arrival_Time  Rem_burstTime   Completed  Original_burstTime  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(proses)):
            for j in range(len(proses[i])):
                print(proses[i][j], end="\t\t\t\t")
            print()
        print(f'Rataan Turnaround Time: {rataaanTurnTime}')
        print(f'Rataan Waiting Time: {rataanWaitTime}')
        print(f'Urutan Proses: {ekseskusiProses}')


if __name__ == "__main__":
    no_of_processes = int(input("Masukan Jumlah Proses : "))
    rr = RoundRobin()
    rr.ProsesData(no_of_processes)