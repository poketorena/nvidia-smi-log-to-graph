import numpy as np
import matplotlib
# matplotlib.use('Agg') # -----(1)
import matplotlib.pyplot as plt
import glob

#
log_file_names = glob.glob('./nvidia-smi_error_time_results/*')


# log_file_names = sorted(glob.glob('./nvidia-smi_gpu-burn_results/200W_120s/*'))
# log_file_names = sorted(glob.glob('./nvidia-smi_gpu-burn_results/250W_120s/*'))


class GpuParameters:
    def __init__(self):
        self.gpu_current_fans = []
        self.gpu_current_temperatures = []
        self.gpu_current_average_powers = []
        self.gpu_seted_max_powers = []
        self.gpu_current_memory_usages = []
        self.gpu_memory_capacitys = []
        self.gpu_current_usages = []


days = []
gpu = []

for _ in range(4):
    gpu.append(GpuParameters())

for file_name in log_file_names:
    file_path = file_name
    with open(file_path) as file:
        for index, line in enumerate(file):
            if index == 0:
                print(line)

                splited_line = line.split(' ')

                if splited_line[0] == 'Unable':
                    for i in range(3):
                        # gpu[i].gpu_current_fans.append(-1)
                        # gpu[i].gpu_current_temperatures.append(-1)
                        # gpu[i].gpu_current_average_powers.append(-1)
                        # gpu[i].gpu_seted_max_powers.append(-1)
                        # gpu[i].gpu_current_memory_usages.append(-1)
                        # gpu[i].gpu_memory_capacitys.append(-1)
                        # gpu[i].gpu_current_usages.append(-1)
                        pass

                day_of_the_week = splited_line[0]
                month = splited_line[1]
                day = splited_line[3]
                time = splited_line[4]
                year = splited_line[5]

                day_data = file_path.split('\\')[1][0:17]
                day_data2 = day_data.replace('_', '')
                day_data3 = day_data2.replace('-', '')

                days.append(day_data3)

            elif index == 8:
                # GPU 0
                print(line)

                splited_line = line.split(' ')

                filtered_1 = filter(lambda x: x != "", splited_line)
                filtered_2 = filter(lambda x: x != "|", filtered_1)
                filtered_3 = filter(lambda x: x != "/", filtered_2)
                filtered_4 = filter(lambda x: x != "|\n", filtered_3)

                filtered_line = list(filtered_4)

                gpu_current_fan = filtered_line[0]
                gpu_current_temperature = filtered_line[1]
                gpu_current_average_power = filtered_line[3]
                gpu_seted_max_power = filtered_line[4]
                gpu_current_memory_usage = filtered_line[5]
                gpu_memory_capacity = filtered_line[6]
                gpu_current_usage = filtered_line[7]

                gpu[0].gpu_current_fans.append(gpu_current_fan.replace('%', ''))
                gpu[0].gpu_current_temperatures.append(gpu_current_temperature.replace('C', ''))
                gpu[0].gpu_current_average_powers.append(gpu_current_average_power.replace('W', ''))
                gpu[0].gpu_seted_max_powers.append(gpu_seted_max_power.replace('W', ''))
                gpu[0].gpu_current_memory_usages.append(gpu_current_memory_usage.replace('MiB', ''))
                gpu[0].gpu_memory_capacitys.append(gpu_memory_capacity.replace('MiB', ''))
                gpu[0].gpu_current_usages.append(gpu_current_usage.replace('%', ''))

                # if int(tmp_tmp) >= 290:
                #     print()

            elif index == 11:
                # GPU 1
                print(line)

                splited_line = line.split(' ')

                filtered_1 = filter(lambda x: x != "", splited_line)
                filtered_2 = filter(lambda x: x != "|", filtered_1)
                filtered_3 = filter(lambda x: x != "/", filtered_2)
                filtered_4 = filter(lambda x: x != "|\n", filtered_3)

                filtered_line = list(filtered_4)

                gpu_current_fan = filtered_line[0]
                gpu_current_temperature = filtered_line[1]
                gpu_current_average_power = filtered_line[3]
                gpu_seted_max_power = filtered_line[4]
                gpu_current_memory_usage = filtered_line[5]
                gpu_memory_capacity = filtered_line[6]
                gpu_current_usage = filtered_line[7]

                gpu[1].gpu_current_fans.append(gpu_current_fan.replace('%', ''))
                gpu[1].gpu_current_temperatures.append(gpu_current_temperature.replace('C', ''))
                gpu[1].gpu_current_average_powers.append(gpu_current_average_power.replace('W', ''))
                gpu[1].gpu_seted_max_powers.append(gpu_seted_max_power.replace('W', ''))
                gpu[1].gpu_current_memory_usages.append(gpu_current_memory_usage.replace('MiB', ''))
                gpu[1].gpu_memory_capacitys.append(gpu_memory_capacity.replace('MiB', ''))
                gpu[1].gpu_current_usages.append(gpu_current_usage.replace('%', ''))

                # if int(tmp_tmp) >= 290:
                #     print()

            elif index == 14:
                # GPU 2
                print(line)

                splited_line = line.split(' ')

                filtered_1 = filter(lambda x: x != "", splited_line)
                filtered_2 = filter(lambda x: x != "|", filtered_1)
                filtered_3 = filter(lambda x: x != "/", filtered_2)
                filtered_4 = filter(lambda x: x != "|\n", filtered_3)

                filtered_line = list(filtered_4)

                gpu_current_fan = filtered_line[0]
                gpu_current_temperature = filtered_line[1]
                gpu_current_average_power = filtered_line[3]
                gpu_seted_max_power = filtered_line[4]
                gpu_current_memory_usage = filtered_line[5]
                gpu_memory_capacity = filtered_line[6]
                gpu_current_usage = filtered_line[7]

                gpu[2].gpu_current_fans.append(gpu_current_fan.replace('%', ''))
                gpu[2].gpu_current_temperatures.append(gpu_current_temperature.replace('C', ''))
                gpu[2].gpu_current_average_powers.append(gpu_current_average_power.replace('W', ''))
                gpu[2].gpu_seted_max_powers.append(gpu_seted_max_power.replace('W', ''))
                gpu[2].gpu_current_memory_usages.append(gpu_current_memory_usage.replace('MiB', ''))
                gpu[2].gpu_memory_capacitys.append(gpu_memory_capacity.replace('MiB', ''))
                gpu[2].gpu_current_usages.append(gpu_current_usage.replace('%', ''))

                # if int(tmp_tmp) >= 290:
                #     print()

            elif index == 17:
                # GPU 3
                print(line)

                splited_line = line.split(' ')

                filtered_1 = filter(lambda x: x != "", splited_line)
                filtered_2 = filter(lambda x: x != "|", filtered_1)
                filtered_3 = filter(lambda x: x != "/", filtered_2)
                filtered_4 = filter(lambda x: x != "|\n", filtered_3)

                filtered_line = list(filtered_4)

                gpu_current_fan = filtered_line[0]
                gpu_current_temperature = filtered_line[1]
                gpu_current_average_power = filtered_line[3]
                gpu_seted_max_power = filtered_line[4]
                gpu_current_memory_usage = filtered_line[5]
                gpu_memory_capacity = filtered_line[6]
                gpu_current_usage = filtered_line[7]

                gpu[3].gpu_current_fans.append(gpu_current_fan.replace('%', ''))
                gpu[3].gpu_current_temperatures.append(gpu_current_temperature.replace('C', ''))
                gpu[3].gpu_current_average_powers.append(gpu_current_average_power.replace('W', ''))
                gpu[3].gpu_seted_max_powers.append(gpu_seted_max_power.replace('W', ''))
                gpu[3].gpu_current_memory_usages.append(gpu_current_memory_usage.replace('MiB', ''))
                gpu[3].gpu_memory_capacitys.append(gpu_memory_capacity.replace('MiB', ''))
                gpu[3].gpu_current_usages.append(gpu_current_usage.replace('%', ''))

                # if int(tmp_tmp) >= 290:
                #     print()

            # else:
            #     raise Exception()

# 折れ線グラフを出力
for index_dayo in range(4):
    gpu[index_dayo].gpu_current_fans = list(map(lambda fan: int(fan), gpu[index_dayo].gpu_current_fans))
    gpu[index_dayo].gpu_current_temperatures = list(map(lambda temperatures: int(temperatures), gpu[index_dayo].gpu_current_temperatures))
    gpu[index_dayo].gpu_current_average_powers = list(map(lambda power: int(power), gpu[index_dayo].gpu_current_average_powers))
    gpu[index_dayo].gpu_seted_max_powers = list(map(lambda max_power: int(max_power), gpu[index_dayo].gpu_seted_max_powers))
    gpu[index_dayo].gpu_current_memory_usages = list(map(lambda memory_usage: int(memory_usage), gpu[index_dayo].gpu_current_memory_usages))
    gpu[index_dayo].gpu_memory_capacitys = list(map(lambda memory_capacity: int(memory_capacity), gpu[index_dayo].gpu_memory_capacitys))
    gpu[index_dayo].gpu_current_usages = list(map(lambda gpu_usage: int(gpu_usage), gpu[index_dayo].gpu_current_usages))

# 描画
for index_dayo in range(4):
    plt.plot(gpu[index_dayo].gpu_current_fans)
    plt.savefig(f'gpu{index_dayo}_gpu_current_fans.png')
    plt.show()

    plt.plot(gpu[index_dayo].gpu_current_temperatures)
    plt.savefig(f'gpu{index_dayo}_gpu_current_temperatures.png')
    plt.show()

    plt.plot(gpu[index_dayo].gpu_current_average_powers)
    plt.savefig(f'gpu{index_dayo}_gpu_current_average_powers.png')
    plt.show()

    plt.plot(gpu[index_dayo].gpu_seted_max_powers)
    plt.savefig(f'gpu{index_dayo}_gpu_seted_max_powers.png')
    plt.show()

    plt.plot(gpu[index_dayo].gpu_current_memory_usages)
    plt.savefig(f'gpu{index_dayo}_gpu_current_memory_usages.png')
    plt.show()

    plt.plot(gpu[index_dayo].gpu_memory_capacitys)
    plt.savefig(f'gpu{index_dayo}_gpu_memory_capacitys.png')
    plt.show()

    plt.plot(gpu[index_dayo].gpu_current_usages)
    plt.savefig(f'gpu{index_dayo}_gpu_current_usages.png')
    plt.show()
