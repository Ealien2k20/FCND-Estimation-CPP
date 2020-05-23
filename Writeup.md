## Write Up: Building an Estimator

<p align="center">
   
  <img width="600" height="450" src="https://user-images.githubusercontent.com/34810513/81973969-85803000-9642-11ea-8052-366fd05f53c1.gif">
  
</p>
This Writeup.md considers the rubric points individually and describes how I addressed each rubric point in my implementation.  

---
### Writeup / README

#### 1. To provide a Writeup that includes all the rubric points and how I addressed each one.  

The current Writeup.md (markdown) file serves the purpose of addressing how I have dealt with the various tasks.

### Implemented Controller

#### 1. Implemented body rate control in C++.

The body rate controller is implemented in the function BodyRateControl. It is a P controller in which a V3F variable called momentCmd is created to contain the moment values provided to the controller. This is calculated by finding the difference between target and the actual body rate values in each axis and multiplying them with the moments of Inertia in each axis to find the target torque. This calculated value is the error value. It is multiplied with the gain of the body rate controller kpPQR to find the target output. After some trial and error, I set the kpPQR values as 85,85 and 5 for P Q and R respectively.

#### 2. Implement roll pitch control in C++.

The roll pitch controller is implemented in the function RollPitchControl(). This is also a p controller where the value to be corrected is the elements R13 and R23 in the rotation matrix R. This is used to accurately control the roll angle and the pitch angle of the controller. The output of this controller is the target value(set point) for the bodyrate controller. Thus the coreection value is translated from the world frame to the body frame through a transformation. The gain value, kpBank for this controller is 12.

After implementing these controllers, the output of the second scenario is as follows. (The Roll could not be made to stay below +/- 0.025 without affecting the results of other scenarios).
<p align="center">
   
  <img width="450" height="352" src="https://user-images.githubusercontent.com/34810513/81974048-a183d180-9642-11ea-9b88-7b85aaf5b78b.gif">
  
</p>

#### 3. Implement altitude controller in C++.
The altitude controller is implemented in the function AltitudeControl(). This is a complete PID controller. The velocity and the position errors are calculated to determine the P and D terms. The position error is integrated to find the I term. The target acceleration is added along with these terms to find the correction term called z_term. This value is then used to calculate the thrust to be applied while accounting for the action of gravity. The difference between the z_term and gravity is divided by R33 to account for the orientation of the vehicle. This is later constrained to stay within the maximum thrust of the drone. The gain values for the controller are 25(kpPosz), 6.5(kpVelz) and 20(KiPosZ).

#### 4. Implement lateral position control in C++.
This controller is a PD controller. It is implemented in the function LateralPositionControl(). This is used to control the drone's X and Y coordinates. The position and velocity errors are calculated. The velocity error is constrained to stay below the maximum XY velocity. The acceleration command is calculated by multiplying the error with the gain terms and it is constrained. The kpPosXY and the kpVelXY gain terms are 30 and 11 respectively.

#### 5. Implement yaw control in C++.
The yaw control calculates the target moment along the Z axis. It is implemented in YawControl() function. The yaw error value is constrained between -2pi and +2pi and it is multiplied with the gain value kpYaw. The kpYaw value is 2.
   
After implementing the altitude, lateral position and the yaw controller, this was the result in scenario 3.

<p align="center">
   
<img width="450" height="352" src="https://user-images.githubusercontent.com/34810513/81974768-a5642380-9643-11ea-8267-160a21080efa.gif">
  
</p>

#### 6. Implement calculating the motor commands given commanded thrust and moments in C++.
The thrust and the moment values calculated by the different P, PD and PID controllers are converted to the motor thrust values in the GenerateMotorCommands() function. The collective thrust and the commanded moment values are used to calculate the c bar, p bar q bar and the r bar values. These 4 values are then used to determine individual thrust values by solving the linear equation using the matrix method.

<p align="center">
   
<img width="450" height="352" src="https://user-images.githubusercontent.com/34810513/81975038-14da1300-9644-11ea-86d8-599d1c5f3139.gif">
  
</p>

### Flight Evaluation

After implementing the above methods, it was time to execute the flight. I was able to complete all the 5 scenarios except controlling the roll of the quad in the 2nd scenrio. This is the result of thee 5th scenario.

<p align="center">
   
  <img width="800" height="600" src="https://user-images.githubusercontent.com/34810513/81974890-d5132b80-9643-11ea-9cea-478a55e0521b.gif">
  
</p>
