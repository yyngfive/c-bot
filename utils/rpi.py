from munch import DefaultMunch
import os
import platform


class System:

    @staticmethod
    def is_RPi() -> bool:
        if platform.system() != 'Linux':
            return False
        with os.popen('uname -a') as p:
            uname = p.read()
            if uname.split()[1] != 'raspberrypi':
                return False
        return True

    @staticmethod
    def get_CPU() -> DefaultMunch:

        temp = os.popen('vcgencmd measure_temp').readline()
        temp = temp.replace("temp=", "").replace("'C\n", "")
        info = dict()
        info['temp'] = temp + '℃'

        usage = str(
            os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())
        info['usage'] = usage + '%'

        return DefaultMunch.fromDict(info)

    @staticmethod
    def get_RAM() -> DefaultMunch:

        with os.popen('free') as p:
            line = p.readlines()[1]
            usage = line.split()[1:4]

        info = dict()

        total = round(int(usage[0]) / 1000, 1)
        used = round(int(usage[1]) / 1000, 1)
        free = round(int(usage[2]) / 1000, 1)

        info['total'] = str(total) + 'MB'
        info['used'] = str(used) + 'MB'
        info['free'] = str(free) + 'MB'
        info['perc'] = str(round(used/total, 3) * 100) + '%'

        return DefaultMunch.fromDict(info)

    @staticmethod
    def get_ROM() -> DefaultMunch:

        with os.popen("df -h /") as p:
            line = p.readlines()[1]
            usage = line.split()[1:5]

        info = dict()

        total = usage[0]
        used = usage[1]
        perc = usage[3]

        info['total'] = total
        info['used'] = used
        info['free'] = str(round(float(total[:-1])-float(used[:-1]), 1))+'G'
        info['perc'] = perc

        return DefaultMunch.fromDict(info)


if __name__ == '__main__':
    print(System.get_CPU())
    print(System.get_RAM())
    print(System.get_ROM())
