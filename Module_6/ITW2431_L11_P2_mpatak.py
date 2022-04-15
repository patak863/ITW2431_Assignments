# Name: Mike Patak
# ITW 2431
# Lab 11 Prob. 2
# File name: ITW2431_L11_P2_mpatak.py
# MODIFIED: 3/31/22
# PURPOSE:  Create a class named "RemoteControl". The class will have five
#           methods, volume_up(), volume_down(), change_channel(), tv_on(),
#           and tv_off(). The program will create a RemoteControl object
#           and it will call the various methods to demonstrate that they
#           are all working correctly. When the TV is turned off and back
#           on the previous volume and channel will be the same.
# ASSUMPTIONS:
###########################################################################

# define the class RemoteControl
class RemoteControl:

    # class constructor
    def __init__(self):
        # initialize the variables
        self.volume_min = 0
        self.volume_max = 5
        self.volume = 3
        self.channel = 10
        self.power = 'off'

    # class method volume_up(), which increases the volume by one count
    def volume_up(self):
        # check if the volume is already at the maximum
        if self.volume < self.volume_max:
            # if volume is less than maximum increase volume by one count
            self.volume += 1
            # print out the message indicating the new volume
            print("Volume increased to: " + str(self.volume))
        else:
            # print output if volume is at maximum
            print("Volume is already at maximum.")

    # class method volume_down(), which decreases the volume by one count
    def volume_down(self):
        # check if the volume is already at the minimum
        if self.volume > self.volume_min:
            # if volume is more than minimum decrease volume by one count
            self.volume -= 1
            # print out the message indicating the new volume
            print("Volume decrease to: " + str(self.volume))
        else:
            # print output if the volume is at minimum
            print("Volume is already at minimum.")

    # class method change_channel(), which will change the TV to a new channel
    def change_channel(self, num):
        # assign the variable a new channel number
        self.channel = num
        # print out the change channel message
        print("Changed channel to: " + str(self.channel))

    # class method tv_on(), which will turn the TV on
    def tv_on(self):
        # assign the self.power variable a value of 'ON'
        self.power = 'ON'
        # print out to the TV on message
        print("TV is on: the volume is: " + str(r.volume) + " and the channel is: " + str(r.channel))

    # class method tv_off(), which will turn the TV off
    def tv_off(self):
        # assign the self.power variable a value of 'OFF'
        self.power = 'OFF'
        # print out the TV off message
        print("TV is off")


# create TV RemoteControl obj
r = RemoteControl()
# execute the RemoteControl methods
r.tv_on()
# test the volume_down() method
r.volume_down()
r.volume_down()
r.volume_down()
r.volume_down()
# test the volume_up() method
r.volume_up()
r.volume_up()
r.volume_up()
r.volume_up()
r.volume_up()
r.volume_up()
# test changing channels
r.change_channel(200)
r.change_channel(255)
# test turning TV off and then back on to see if previous
# volume and channel are unchanged
r.tv_off()
r.tv_on()
# Name: Mike Patak
# ITW 2431
# Lab 11 Prob. 2
# File name: ITW2431_L11_P2_mpatak.py
# MODIFIED: 3/31/22
# PURPOSE:  Create a class named "RemoteControl". The class will have five
#           methods, volume_up(), volume_down(), change_channel(), tv_on(),
#           and tv_off(). The program will create a RemoteControl object
#           and it will call the various methods to demonstrate that they
#           are all working correctly. When the TV is turned off and back
#           on the previous volume and channel will be the same.
# ASSUMPTIONS:
###########################################################################

# define the class RemoteControl
class RemoteControl:

    # class constructor
    def __init__(self):
        # initialize the variables
        self.volume_min = 0
        self.volume_max = 5
        self.volume = 3
        self.channel = 10
        self.power = 'off'

    # class method volume_up(), which increases the volume by one count
    def volume_up(self):
        # check if the volume is already at the maximum
        if self.volume < self.volume_max:
            # if volume is less than maximum increase volume by one count
            self.volume += 1
            # print out the message indicating the new volume
            print("Volume increased to: " + str(self.volume))
        else:
            # print output if volume is at maximum
            print("Volume is already at maximum.")

    # class method volume_down(), which decreases the volume by one count
    def volume_down(self):
        # check if the volume is already at the minimum
        if self.volume > self.volume_min:
            # if volume is more than minimum decrease volume by one count
            self.volume -= 1
            # print out the message indicating the new volume
            print("Volume decrease to: " + str(self.volume))
        else:
            # print output if the volume is at minimum
            print("Volume is already at minimum.")

    # class method change_channel(), which will change the TV to a new channel
    def change_channel(self, num):
        # assign the variable a new channel number
        self.channel = num
        # print out the change channel message
        print("Changed channel to: " + str(self.channel))

    # class method tv_on(), which will turn the TV on
    def tv_on(self):
        # assign the self.power variable a value of 'ON'
        self.power = 'ON'
        # print out to the TV on message
        print("TV is on: the volume is: " + str(r.volume) + " and the channel is: " + str(r.channel))

    # class method tv_off(), which will turn the TV off
    def tv_off(self):
        # assign the self.power variable a value of 'OFF'
        self.power = 'OFF'
        # print out the TV off message
        print("TV is off")


# create TV RemoteControl obj
r = RemoteControl()
# execute the RemoteControl methods
r.tv_on()
# test the volume_down() method
r.volume_down()
r.volume_down()
r.volume_down()
r.volume_down()
# test the volume_up() method
r.volume_up()
r.volume_up()
r.volume_up()
r.volume_up()
r.volume_up()
r.volume_up()
# test changing channels
r.change_channel(200)
r.change_channel(255)
# test turning TV off and then back on to see if previous
# volume and channel are unchanged
r.tv_off()
r.tv_on()