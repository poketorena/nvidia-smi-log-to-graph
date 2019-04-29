from typing import List

import matplotlib.pyplot as plt
import glob
from datetime import datetime
import matplotlib.dates as mdates
import os

log_file_names = glob.glob('./nvidia-smi_error_time_results/*')

# log_file_names = sorted(glob.glob('./nvidia-smi_gpu-burn_results/200W_120s/*'))
# log_file_names = sorted(glob.glob('./nvidia-smi_gpu-burn_results/250W_120s/*'))

datetime_now = datetime.now()

# 赤い点線（デッドライン）の設定

# 0から線を引く
xmin = 0
# ログファイルの数まで線を引く
xmax = len(log_file_names)
# 消費電力の上限
gpu1_power_upper_limit = 250
# GPU4個
multi_gpu_power_upper_limit = gpu1_power_upper_limit * 4
# GPUの温度の上限
gpu_temperature_upper_limit = 90


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

        plt.plot(gpu_parameter.current_fan_speeds, label='GPU fan speed')
        plt.legend()
        plt.title('The relationship between time and GPU fan speed')
        plt.xlabel('Number of log files')
        plt.ylabel('GPU fan speed [%]')
        plt.savefig(f'{save_directory_path}/gpu{index}_current_fans.png')
        plt.show()

        plt.plot(gpu_parameter.current_temperatures, label='GPU temperature')
        plt.legend()
        plt.title('The relationship between time and GPU temperature')
        plt.xlabel('Number of log files')
        plt.ylabel('GPU temperature [℃]')
        plt.hlines([gpu_temperature_upper_limit], xmin, xmax, "red", linestyles='dashed')
        plt.savefig(f'{save_directory_path}/gpu{index}_current_temperatures.png')
        plt.show()

        plt.plot(gpu_parameter.current_average_powers, label='GPU power')
        plt.legend()
        plt.title('The relationship between time and GPU power')
        plt.xlabel('Number of log files')
        plt.ylabel('GPU power [W]')
        plt.hlines([gpu1_power_upper_limit], xmin, xmax, "red", linestyles='dashed')
        plt.savefig(f'{save_directory_path}/gpu{index}_current_average_powers.png')
        plt.show()

        plt.plot(gpu_parameter.seted_max_powers, label='GPU power')
        plt.legend()
        plt.title('The relationship between time and GPU max power')
        plt.xlabel('Number of log files')
        plt.ylabel('GPU power [W]')
        plt.savefig(f'{save_directory_path}/gpu{index}_seted_max_powers.png')
        plt.show()

        plt.plot(gpu_parameter.current_memory_usages, label='GPU memory usage')
        plt.legend()
        plt.title('The relationship between time and GPU memory usage')
        plt.xlabel('Number of log files')
        plt.ylabel('GPU memory usage [MiB]')
        plt.savefig(f'{save_directory_path}/gpu{index}_current_memory_usages.png')
        plt.show()

        plt.plot(gpu_parameter.memory_capacitys, label='GPU memory usage')
        plt.legend()
        plt.title('The relationship between time and GPU memory capacity')
        plt.xlabel('Number of log files')
        plt.ylabel('GPU memory usage [MiB]')
        plt.savefig(f'{save_directory_path}/gpu{index}_memory_capacitys.png')
        plt.show()

        plt.plot(gpu_parameter.current_usages, label='GPU memory usage')
        plt.legend()
        plt.title('The relationship between time and GPU memory usage')
        plt.xlabel('Number of log files')
        plt.ylabel('GPU memory usage [MiB]')
        plt.savefig(f'{save_directory_path}/gpu{index}_current_usages.png')
        plt.show()


datetimes: List[datetime] = []
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
                    for i in range(4):
                        gpu_parameters_collection[i].current_fan_speeds.append(0)
                        gpu_parameters_collection[i].current_temperatures.append(0)
                        gpu_parameters_collection[i].current_average_powers.append(0)
                        gpu_parameters_collection[i].seted_max_powers.append(0)
                        gpu_parameters_collection[i].current_memory_usages.append(0)
                        gpu_parameters_collection[i].memory_capacitys.append(0)
                        gpu_parameters_collection[i].current_usages.append(0)

                day_of_the_week = splited_line[0]
                month = splited_line[1]
                day = splited_line[3]
                time = splited_line[4]
                year = splited_line[5]

                day_data = file_name.split('\\')[1][0:17]
                day_data2 = day_data.replace('_', '')
                day_data3 = day_data2.replace('-', '')

                year = int(day_data3[0:4])
                month = int(day_data3[4:6])
                day = int(day_data3[6:8])
                hour = int(day_data3[8:10])
                minute = int(day_data3[10:12])
                second = int(day_data3[12:14])
                datetime_data = datetime(year, month, day, hour, minute, second)

                if not splited_line[0] == 'Unable':
                    datetimes.append(datetime_data)

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

# 4つのGPUの消費電力の合計のグラフ（以下は抽象化に失敗したコード、DRY原則難しい...）

gpu_current_average_power_sums = []

for index in range(len(gpu_parameters_collection[0].current_average_powers)):

    gpu_current_average_power_sum = 0

    for gpu_index2 in range(4):
        gpu_current_average_power_sum += gpu_parameters_collection[gpu_index2].current_average_powers[index]

    gpu_current_average_power_sums.append(gpu_current_average_power_sum)

save_directory_path = f'./graph/{datetime_now.year}/{datetime_now.month}/{datetime_now.day}/{datetime_now.hour}_{datetime_now.minute}_{datetime_now.second}/gpus_power_sum'

if not os.path.isdir(save_directory_path):
    os.makedirs(save_directory_path)

fig, ax = plt.subplots()
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d\n%H:%M:%s'))

ax.plot(gpu_current_average_power_sums, label='Sum of power consumption of 4 GPUs')
# ax.plot(datetimes, gpu_current_average_power_sums, label='Sum of power consumption of 4 GPUs')

# Formatterでx軸の日付ラベルを月・日に設定

# xfmt = mdates.DateFormatter("%m/%d")
#
# # DayLocatorで間隔を日数に
# xloc = mdates.DayLocator()
#
#
# ax.xaxis.set_major_locator(xloc)
# ax.xaxis.set_major_formatter(xfmt)

ax.legend()
ax.set_title('The relationship between time and the power consumption of the four GPUs')
ax.set_xlabel('Time')
ax.set_ylabel('Sum of power consumption of 4 GPUs [W]')
ax.hlines([multi_gpu_power_upper_limit], xmin, xmax, "red", linestyles='dashed')
fig.savefig(f'{save_directory_path}/gpu_current_average_power_sums.png')
fig.show()

exit()
