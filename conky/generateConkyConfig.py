import os

contents = R"""
conky.config = {
	update_interval = 2.0,
	xinerama_head=1,
	own_window = true,
	own_window_class = 'Conky',
	own_window_type = 'desktop',
    own_window_argb_visual = true,
	own_window_argb_value = 50,
	own_window_hints = 'undecorated,below,sticky,skip_taskbar,skip_pager',
	border_inner_margin = 10,
	border_outer_margin = 0,
	stippled_borders = 0,
	double_buffer = true,
    alignment = 'top_right',
    background = false,
    border_width = 1,
    cpu_avg_samples = 2,
	default_color = 'white',
    default_outline_color = 'white',
    default_shade_color = 'white',
    draw_borders = false,
    draw_graph_borders = true,
    draw_outline = false,
    draw_shades = false,
    use_xft = true,
    xftalpha = 0.8,
    font = 'Ubuntu Mono:size=12',
    gap_x = 20,
    gap_y = 60,
	minimum_width = 450,
    minimum_height = 500,
    net_avg_samples = 2,
    no_buffers = true,
    out_to_console = false,
    out_to_stderr = false,
    extra_newline = false,
    uppercase = false,
    use_spacer = 'none',
    show_graph_scale = true,
    show_graph_range = true
}

conky.text = [[
#
# SYSTEM
#
${font sans-serif:bold:size=15}SYSTEM ${hr 2}${font sans-serif:bold:size=10}
${color grey}Host:$color $alignr $nodename
${color grey}Uptime:$color $alignr $uptime
${color grey}Processes:$color $alignr $processes
${color grey}Running:$color $alignr $running_processes
#
# CPU
#
${font sans-serif:bold:size=15}CPU ${hr 2}${font sans-serif:bold:size=10}
${color grey}${execp ~/git/linutils/conky/cpuName}$color
${color grey}Frequency:$color $alignr $freq_g GHz
${color grey}Temperature:$color $alignr ${hwmon pch_skylake temp 1} C
${color grey}Load:$color $alignr $cpu%
${cpugraph}
#
# GPU
#
${font sans-serif:bold:size=15}GPU ${hr 2}${font sans-serif:bold:size=10}
${color grey}${execp ~/git/linutils/conky/gpuName}$color
${color grey}Load:$color $alignr ${execp ~/git/linutils/conky/gpuUsage} %
${color grey}Memory:$color $alignr ${execp ~/git/linutils/conky/gpuMemory} %
${color grey}Temperature:$color $alignr ${execp ~/git/linutils/conky/gpuTemp} C
#
# MEMORY
#
${font sans-serif:bold:size=15}MEMORY ${hr 2}${font sans-serif:bold:size=10}
${color grey}RAM:$color ${goto 75} $mem/$memmax ${goto 250} $memperc% ${goto 350}${membar 4}
${color grey}Swap:$color ${goto 75} $swap/$swapmax ${goto 250} $swapperc% ${goto 350}${swapbar 4}
#
# FILE SYSTEM
#
${font sans-serif:bold:size=15}FILE SYSTEM ${hr 2}${font sans-serif:bold:size=10}
${color grey}/ ${goto 225} $color${fs_used /}/${fs_size /} ${goto 385}${fs_bar 4 /}
${if_existing /run/media/mate/linux_hdd}\
${color grey}linux_hdd $color ${goto 225} ${fs_used /run/media/mate/linux_hdd}/${fs_size /run/media/mate/linux_hdd} ${goto 385}${fs_bar 4 /run/media/mate/linux_hdd}\
${endif}
${if_existing /run/media/mate/windows_hdd}\
${color grey}windows_hdd $color ${goto 225} ${fs_used /run/media/mate/windows_hdd}/${fs_size /run/media/mate/windows_hdd} ${goto 385}${fs_bar 4 /run/media/mate/windows_hdd}\
${endif}
#
# NETWORK
#
${font sans-serif:bold:size=15}NETWORK ${hr 2}${font sans-serif:bold:size=10}
${color grey}WiFi Down:$color $alignr ${downspeed WIRELESS_DEVICE_NAME}
${color grey}WiFi Up:$color $alignr ${upspeed WIRELESS_DEVICE_NAME}
${color grey}Ethernet Down:$color $alignr ${downspeed ETHERNET_DEVICE_NAME}
${color grey}Ethernet Up:$color $alignr ${upspeed ETHERNET_DEVICE_NAME}
${color grey}External IP: $color $alignr ${execi 1000  wget -q -O- http://ipecho.net/plain; echo}
#
# PROCESSES
#
${font sans-serif:bold:size=15}PROCESSES ${hr 2}${font sans-serif:bold:size=10}
${color grey}Name $alignr PID   CPU%   MEM%${color}
${top name 1} $alignr ${top pid 1}   ${top cpu 1}    ${top mem 1}
${top name 2} $alignr ${top pid 2}   ${top cpu 2}    ${top mem 2}
${top name 3} $alignr ${top pid 3}   ${top cpu 3}    ${top mem 3}
]]
""".replace(
    "ETHERNET_DEVICE_NAME", os.popen(R"""ip link | awk -F: '$0 !~ "lo|vir|wl|^[^0-9]"{print $2;getline}'""").read().strip()
).replace(
    "WIRELESS_DEVICE_NAME", os.popen(R"""iw dev | awk '$1=="Interface"{print $2}'""").read().strip()
)

print(contents)
