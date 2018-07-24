#! /usr/bin/python

""" checking battery life and altering if too low """
import subprocess

acpi_values = subprocess.check_output(['acpi'])
acpi_values_list = acpi_values.split(",")
battery_count = acpi_values_list[1]
battery_count = battery_count.replace("%", "")

print battery_count

if int(battery_count) < 16:
	subprocess.call(['notify-send "Low Battery"'], shell=True)


"""
- cronjob to run every 2 min.
"""
