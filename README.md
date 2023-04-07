# Blood_oxygen_module_anz
## Abstract
It's a program written by python and PyQt to find some ways to evaluate the Blood-oxygen module by the data the module collects and do some physiological information analysis.  
The Blood-oxygen module I used is MAX30101. It's a commercial blood-oxygen module,so the accurancy of the data is acceptable.This module can provide led control,current control,pulse control,and etc.You can see the outlines about it on Maxim's website.I use it to collect the PPG signals from my thumb in static.I use current control to collect the datas of 20mA and 40mA , and my sample rate is 100Hz.Each one has datas of IR(930nm) , red(655nm),and green(520nm).Figure out some ways to analyse the relatons between color light with different currents , and do some algorithms to show physiological information from the data of the MAX30101.  
## Content  
### 1.Design a program to analyse the data from MAX30101 in many ways.My interfarce and the usage of the program are below(It's made of Python and PyQt):   
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/Data_Load.PNG)  
### 2.The Introduction of functions:  
#### (1).Intensity:    
I collect the intensity variety of three kinds of light and different currents
(__make sure your data without white cell because I didn't block for it__).
The result is below:    
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/intensity.PNG)  
The PPG signal is apparent,but it's diffirent from each other.  
#### (2).Fast Fourier Transform(FFT):  
I set some thresholds for peak detections , and they will show on the chart(they will show their site).We can see the blood resonance.But The maximum is near 1Hz.It seems that green light is more sensitive to variety,because it has more peaks tagging on the chart.That means more peaks are above threshold.In 40mA current,it seems that more frequency will appear.  
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/FFT_peak.PNG)  
#### (3).Short-Time Fourier Transform(STFT):  
It's a way to create time window shifting to compute FFT ,and it can obtain time,frequency,and intensity of frequency in the same time.I present it on the 3D chart.  
We can see The frequency of gree light is more stable than the other lights,and the frequency of gree light is more stable at 40 mA.
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/STFT.PNG)  
#### (4).Wavelet transform:  
It's a way to use a fast decay wavelet to get time,frequency,and intensity of frequency information.Using small wavelet is more corrent and continuous instead of using periodic  function.Because I plot 3D in STFT,this time I plot contour map(STFT can also plot contour map).In contour map, we could see the traits I mentioned in (3) obviously.  
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/Wavelet%20transform.PNG )  
#### (5).PI、Heart rate、SNR、SpO2:  
You can just see my summarize in the bottom.  
##### i.PI is a index to show AC/DC in PPG signals,and it can indicate your vascular perfusion.The concept is below(出自:行政院國家科學委員會):  
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/AC%26DC.PNG)    
I compute the avarage of the PI in every set on charts except sets which are not pairs.The result is below:    
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/PI.PNG)  
##### II.The Heart rate result is below:  
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/Heart%20rate.PNG )  

##### III.SNR:
I use welch and FFT ways to compute the power density in frequency domain.  Welch is a way to use window shifting to compute the power density in frequency domain,and you can see more details in the website.I regard 0.8~2.5Hz as my signal range and others as noise , and compute SNR=10*log(P_signal/P_noise).The result is below:  
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/SNR.PNG ) 
##### IV.SpO2:  
It needs IR and red light.The concept is below:  
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/AC%26DC2.PNG )   
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/formula.PNG )  
You could also measure many times in full oxygen surrounding using regression methods to optain coefficients a,b,and c. I use the coefficients Maxim provides.
The result is below:  
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/SpO2.gif ) 
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/SpO2_data.PNG)
### Summarize PI、Heart rate、SNR、SpO2 :  
![image](https://github.com/Ray0124/Blood_oxygen_module_anz/blob/main/sum.PNG)  

## Conclusion:
 1.It seems that green light is good at PI,HR,SNR comparing with Red and IR light,but the penetration of red and ir light is better than green light's and than green light is easy to be absorbed by melanin according to the literature.That means green light is more sensitive to PPG , but need more light to penetrate skin.On the other hand,the SpO2 of 20mA is better than 40mA's.Obviously current can boost the intensity of light, but it will also boost DC level to affect the performance of the AC level.That means we need to find a way to adjust current following the skin of subject to do the best performance.  
 2.Current increasing may increase other frequency into the frequency of the blood resonance.It will affect frequency and AC-part of the PPG signal.  
 3.Maybe wavelet transform charts can be feature maps for feature extraction and combined with datas above to do some analysis or machine learning and etc for Blood-oxygen device performances or for light switching with the skin condition(eg:dark skin,it will use more penetrable light). 
  
   
  





