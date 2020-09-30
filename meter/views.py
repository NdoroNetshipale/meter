    #!/usr/bin/python3
    #Loading modbus library
    #Initializing searial communication on the modbus library
from django.shortcuts import render
import  minimalmodbus
from datetime import datetime
from django.http import HttpResponse

def button(request):
    return render(request,'home.html')

def output(request):


    sdm630 = minimalmodbus.Instrument('/dev/ttyUSB1', 1)
    sdm630.serial.baudrate = 9600
    sdm630.serial.bytesize = 8
    sdm630.serial.parity = minimalmodbus.serial.PARITY_NONE
    sdm630.serial.stopbits = 1
    sdm630.serial.timeout = 1
    sdm630.debug = False
    sdm630.mode = minimalmodbus.MODE_RTU
    print(sdm630)



    def main():
        Volts = sdm630.read_float(0, functioncode=4)
        Current = sdm630.read_float(6, functioncode=4)
        Active_Power = sdm630.read_float(12, functioncode=4)
        Apparent_Power = sdm630.read_float(18, functioncode=4)
        Reactive_Power = sdm630.read_float(24, functioncode=4)
        Power_Factor = sdm630.read_float(30, functioncode=4)
        Phase_Angle = sdm630.read_float(36, functioncode=4)
        Frequency = sdm630.read_float(70, functioncode=4)
        Import_Active_Energy = sdm630.read_float(72, functioncode=4)
        Export_Active_Energy = sdm630.read_float(74, functioncode=4)
        Import_Reactive_Energy = sdm630.read_float(76, functioncode=4)
        Export_Reactive_Energy = sdm630.read_float(78, functioncode=4)
        Total_Active_Energy = sdm630.read_float(342, functioncode=4)
        Total_Reactive_Energy = sdm630.read_float(344, functioncode=4)

        print('Voltage: {0:.1f} Volts   '.format(Volts))
        print('Current: {0:.1f} Amps    '.format(Current))
        print('Active power: {0:.1f} Watts    '.format(Active_Power))
        print('Apparent power: {0:.1f} VoltAmps    '.format(Apparent_Power))
        print('Reactive power: {0:.1f} VAr    '.format(Reactive_Power))
        print('Power factor: {0:.1f}      '.format(Power_Factor))
        print('Phase angle: {0:.1f} Degree      '.format(Phase_Angle))
        print('Frequency: {0:.1f} Hz      '.format(Frequency))
        print('Import active energy: {0:.3f} Kwh     '.format(Import_Active_Energy))
        print('Export active energy: {0:.3f} kwh    '.format(Export_Active_Energy))
        print('Import reactive energy: {0:.3f} kvarh   '.format(Import_Reactive_Energy))
        print('Export reactive energy: {0:.3f} kvarh    '.format(Export_Reactive_Energy))
        print('Total active energy: {0:.3f} kwh     '.format(Total_Active_Energy))
        print('Total reactive energy: {0:.3f} kvarh'.format(Total_Reactive_Energy))
        print('Current Yield (V*A): {0:.1f} Watt'.format(Volts * Current))
  
       
        Output =open('./data.txt','w')
        Output.writelines('Voltage: {0:.1f} Volts      '.format(Volts))
        Output.writelines('')
        Output.writelines ('Current: {0:.1f} Amps     '.format(Current))
        Output.writelines('')
        Output.writelines('Active power: {0:.1f} Watts     '.format(Active_Power))
        Output.writelines('')
        Output.writelines('Apparent power: {0:.1f} VoltAmps     '.format(Apparent_Power))
        Output.writelines(' ')
        Output.writelines('Reactive power: {0:.1f} VAr   '.format(Reactive_Power))
        Output.writelines(' ')
        Output.writelines('Power factor: {0:.1f}     '.format(Power_Factor))
        Output.writelines(' ')
        Output.writelines('Phase angle: {0:.1f} Degree    '.format(Phase_Angle))
        Output.writelines(' ')
        Output.writelines('Frequency: {0:.1f} Hz    '.format(Frequency))
        Output.writelines(' ')
        Output.writelines('Import active energy: {0:.3f} Kwh     '.format(Import_Active_Energy))
        Output.writelines(' ')
        Output.writelines('Export active energy: {0:.3f} kwh      '.format(Export_Active_Energy))
        Output.writelines(' ')
        Output.writelines('Import reactive energy: {0:.3f} kvarh     '.format(Import_Reactive_Energy))
        Output.writelines(' ')
        Output.writelines('Export reactive energy: {0:.3f} kvarh   '.format(Export_Reactive_Energy))
        Output.writelines(' ')
        Output.writelines('Total active energy: {0:.3f} kwh     '.format(Total_Active_Energy))
        Output.writelines(' ')
        Output.writelines('Total reactive energy: {0:.3f} kvarh   '.format(Total_Reactive_Energy))
        Output.writelines(' ')
        Output.writelines('Current Yield (V*A): {0:.1f} Watt     '.format(Volts * Current))
        Output.writelines(' ')
        Output.close()

    def filereader():
                readfile= open('./data.txt','r')
                data_ = HttpResponse(readfile.readlines(),content_type="text/plain")
                readfile.close()
                print(data_.content)
                return data_
    
    main()
    data =filereader()
    return render(request,'home.html', {'data':data.content})

