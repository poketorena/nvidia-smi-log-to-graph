from typing import List

import matplotlib.pyplot as plt
import glob
from datetime import datetime
import os

log_file_names = glob.glob('./nvidia-smi_error_time_results/*')

# log_file_names = sorted(glob.glob('./nvidia-smi_gpu-burn_results/200W_120s/*'))
# log_file_names = sorted(glob.glob('./nvidia-smi_gpu-burn_results/250W_120s/*'))

datetime_now = datetime.now()


class GpuParameters:
    def __init__(self):
        self.current_fan_speeds = []
        self.current_temperatures = []
        self.current_average_powers = []
        self.seted_max_powers = []
        self.current_memory_usages = []
        self.memory_capacitys = []
        self.current_usages = []


def parse_and_add_gpu_parameters(line: str, gpu_index: int) -> None:
    splited_line = line.split(' ')

    filtered_1 = filter(lambda x: x != "", splited_line)
    filtered_2 = filter(lambda x: x != "|", filtered_1)
    filtered_3 = filter(lambda x: x != "/", filtered_2)
    filtered_4 = filter(lambda x: x != "|\n", filtered_3)

    filtered_line = list(filtered_4)

    gpu_current_fan_speed = int(filtered_line[0].replace('%', ''))
    gpu_current_temperature = int(filtered_line[1].replace('C', ''))
    gpu_current_average_power = int(filtered_line[3].replace('W', ''))
    gpu_seted_max_power = int(filtered_line[4].replace('W', ''))
    gpu_current_memory_usage = int(filtered_line[5].replace('MiB', ''))
    gpu_memory_capacity = int(filtered_line[6].replace('MiB', ''))
    gpu_current_usage = int(filtered_line[7].replace('%', ''))

    gpu_parameters_collection[gpu_index].current_fan_speeds.append(gpu_current_fan_speed)
    gpu_parameters_collection[gpu_index].current_temperatures.append(gpu_current_temperature)
    gpu_parameters_collection[gpu_index].current_average_powers.append(gpu_current_average_power)
    gpu_parameters_collection[gpu_index].seted_max_powers.append(gpu_seted_max_power)
    gpu_parameters_collection[gpu_index].current_memory_usages.append(gpu_current_memory_usage)
    gpu_parameters_collection[gpu_index].memory_capacitys.append(gpu_memory_capacity)
    gpu_parameters_collection[gpu_index].current_usages.append(gpu_current_usage)


def plot_and_save_line_graph(gpu_parameters_collection: List[GpuParameters]) -> None:
    # 折れ線グラフを描画
    for index, gpu_parameter in enumerate(gpu_parameters_collection):
        save_directory_path = f'./graph/{datetime_now.year}/{datetime_now.month}/{datetime_now.day}/{datetime_now.hour}_{datetime_now.minute}_{datetime_now.second}/gpu{index}'

        if not os.path.isdir(save_directory_path):
            os.makedirs(save_directory_path)

        plt.plot(gpu_parameter.current_fan_speeds)
        plt.savefig(f'{save_directory_path}/gpu{index}_current_fans.png')
        plt.show()

        plt.plot(gpu_parameter.current_temperatures)
        plt.savefig(f'{save_directory_path}/gpu{index}_current_temperatures.png')
        plt.show()

        plt.plot(gpu_parameter.current_average_powers)
        plt.savefig(f'{save_directory_path}/gpu{index}_current_average_powers.png')
        plt.show()

        plt.plot(gpu_parameter.seted_max_powers)
        plt.savefig(f'{save_directory_path}/gpu{index}_seted_max_powers.png')
        plt.show()

        plt.plot(gpu_parameter.current_memory_usages)
        plt.savefig(f'{save_directory_path}/gpu{index}_current_memory_usages.png')
        plt.show()

        plt.plot(gpu_parameter.memory_capacitys)
        plt.savefig(f'{save_directory_path}/gpu{index}_memory_capacitys.png')
        plt.show()

        plt.plot(gpu_parameter.current_usages)
        plt.savefig(f'{save_directory_path}/gpu{index}_current_usages.png')
        plt.show()


days = []
gpu_parameters_collection = []

for _ in range(4):
    gpu_parameters_collection.append(GpuParameters())

for file_name in log_file_names:
    with open(file_name) as file:
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

                day_data = file_name.split('\\')[1][0:17]
                day_data2 = day_data.replace('_', '')
                day_data3 = day_data2.replace('-', '')

                days.append(day_data3)

            elif index == 8:
                # GPU 0
                gpu_index = 0
                print(line)
                parse_and_add_gpu_parameters(line, gpu_index)

            elif index == 11:
                # GPU 1
                gpu_index = 1
                print(line)
                parse_and_add_gpu_parameters(line, gpu_index)

            elif index == 14:
                # GPU 2
                gpu_index = 2
                print(line)
                parse_and_add_gpu_parameters(line, gpu_index)

            elif index == 17:
                # GPU 3
                gpu_index = 3
                print(line)
                parse_and_add_gpu_parameters(line, gpu_index)

plot_and_save_line_graph(gpu_parameters_collection)

# 4つのGPUの消費電力の合計のグラフ

gpu_current_average_power_sums = []

for index in range(len(gpu_parameters_collection[0].current_average_powers)):

    gpu_current_average_power_sum = 0

    for gpu_index2 in range(4):
        gpu_current_average_power_sum += gpu_parameters_collection[0].current_average_powers[index]

    gpu_current_average_power_sums.append(gpu_current_average_power_sum)


save_directory_path = f'./graph/{datetime_now.year}/{datetime_now.month}/{datetime_now.day}/{datetime_now.hour}_{datetime_now.minute}_{datetime_now.second}/gpus_power_sum'

if not os.path.isdir(save_directory_path):
    os.makedirs(save_directory_path)

plt.plot(gpu_current_average_power_sums)
plt.savefig(f'{save_directory_path}/gpu_current_average_power_sums.png')
plt.show()

exit()
