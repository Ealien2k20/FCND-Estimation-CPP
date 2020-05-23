## Write Up: Building an Estimator

This Writeup.md considers the rubric points individually and describes how I addressed each rubric point in my implementation.  

---
### Writeup / README

#### 1. To provide a Writeup that includes all the rubric points and how I addressed each one.  

The current Writeup.md (markdown) file serves the purpose of addressing how I have dealt with the various tasks.

### Implement Estimator

#### 1. Determine the standard deviation of the measurement noise of both GPS X data and Accelerometer X data.
In order to calculate the standard deviation of the measurement noise, I wrote a python script called as standev.py in config/log. Basically I obtained the text from both Graph1.txt and Graph2.txt which were obtained after running scenario 06_SensorNoise for around t=9s and extracted the 2nd column from each text file which contains the sensor readings from the GPS and Accelerometer respectively. I converted the string values to float and appended them to an empty list and coverted the list to numpy arrays. I used numpy's .std() member function to get the standard deviation from each array. After executing the program, the Standard deviations of the GPS and Accelerometer were found to be 0.68 and 0.49 respectively. After updating the new values in 06_SensorNoise.txt, the result captured approximately 68% of the sensor measurements as shown below:

<p align="center">
   
  <img width="600" height="450" src="https://user-images.githubusercontent.com/34810513/82730162-5ab96a00-9d1b-11ea-8fc3-d1916d062595.gif">
  
</p>

#### 2. Implement a better rate gyro attitude integration scheme in the UpdateFromIMU() function.
In the UpdateFromIMU() function of QuadEstimatorEKF.cpp, I have converted the angular velocity values obtained from the gyro sensor corresponding to the body frame(gyro.x,gyro.y,gyro.z) to its values corresponding to the inertial frame(phi_dot,theta_dot,psi_dot) using the rotational matrix transformation. After that I used these values to integrate the current estimated roll pitch and yaw angles for the time duration dtIMU. The yaw angle is normalised after integration to lie inbetween -pi and +pi. The improved integration scheme resulted in an attitude estimator of < 0.1 rad for each of the Euler angles for a duration of at least 3 seconds during the simulation as shown below:

<p align="center">
   
  <img width="450" height="352" src="https://user-images.githubusercontent.com/34810513/82730180-876d8180-9d1b-11ea-88c5-9bf87782a9b6.gif">
  
</p>

#### 3. Implement all of the elements of the prediction step for the estimator.
The prediction step has been implemented in the functions PredictState(), GetRbgPrime() and Predict() which updates the current state, calculates the RbgPrime 3x3 matrix and performns the predict steps of the Extended Kalman filter respectively. PredictState() performs double integration on the x,y and z axis acceleration to calculate the new velocity and position. RbgPrime 3x3 matrix is calculated using the current roll pitch and yaw values. The Predict function updates the covariance using RbgPrime and gprime matrices. The formulae is ekfCov = gPrime*ekfCov*gPrime.transpose()+Q. After that I updated the QPosXYStd as 0.01 and the QVelXYStd as .2. The result of the scenario 09_PredictionCov is shown below:

<p align="center">
   
  <img width="450" height="352" src="https://user-images.githubusercontent.com/34810513/82730199-a409b980-9d1b-11ea-9bc0-68e410887ec4.gif">
  
</p>

#### 4. Implement the magnetometer update.
The magnetometer update is performed in UpdateFromMag() function. The hprime vector's last value is updated as 1 and the zFromX value is set as the yaw value in ekfState. The yaw error is calculated as the difference between the yaw value given by the sensor and the zFromX value. The yaw value is normalised to lie inbetween -pi and pi. The z,hprime and zFromX values are sent to the Update() function which updates the yaw angle of the quadcopter using the calculated Kalman gain. After setting the QYawStd as .15, the results of the scenario 10_MagUpdate is shown below:

<p align="center">
   
  <img width="450" height="352" src="https://user-images.githubusercontent.com/34810513/82730214-c7ccff80-9d1b-11ea-8873-585a6dae9968.gif">
  
</p>

#### 5. Implement the GPS update.
The UpdateFromGPS the z values are updated with the GPS sensor measurements and the hprime matrix's diagonal elements are filled with ones. The zFromX values are filled with the predicted x,y,z position and velocity values. Similar to the UpdateFromMag(), these values are sent to the Update() function. After this I have added my own controller from project 3.

### Flight Evaluation

#### 1. Meet the performance criteria of each step.
The estimator which I have implemented meets the performance criteria of each step. This shows that I have succesfully implemented the Extended Kalman Filter and the Complementary filter to estimate the state of the quad.


#### 2. De-tune your controller to successfully fly the final desired box trajectory with your estimator and realistic sensors.
After replacing the controller with my ideal controller, the performance of the drone was not ideal. The new tuned values are kpPosXY = 4, kpPosZ = 19.5, KIPosZ = 27,kpVelXY = 11, kpVelZ = 6.75, kpBank = 9.4, kpYaw = 3 and kpPQR = 78,78,6.5. After tuning the control the result of scenario 11_GPSUpdate is shown:

<p align="center">
   
  <img width="450" height="352" src="https://user-images.githubusercontent.com/34810513/82730281-1da1a780-9d1c-11ea-9ab4-fbd35b90ef5f.gif">
  
</p>

