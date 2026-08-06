# 📸 Project Screenshots

---

## 🏗️ AWS Cloud Monitoring System Architecture

This architecture illustrates the complete monitoring workflow. The Python application running on an Amazon EC2 instance generates logs, which are collected by the CloudWatch Agent. The logs are sent to Amazon CloudWatch Logs, where Metric Filters transform log events into custom metrics. CloudWatch Alarms continuously monitor these metrics and trigger Amazon SNS email notifications whenever predefined thresholds are exceeded.


<img width="732" height="1026" alt="architecture (2)" src="https://github.com/user-attachments/assets/71b28705-ebee-45de-bd4b-5f75713792b8" />

---

## 🖥️ Amazon EC2 Instance

The monitoring application is hosted on an Amazon EC2 instance. This virtual server runs the Python log generator and the CloudWatch Agent responsible for forwarding application logs to Amazon CloudWatch.


<img width="1912" height="976" alt="EC2 instance" src="https://github.com/user-attachments/assets/91429026-8146-465d-bf14-ad7bbd947cac" />

---

## ⚙️ CloudWatch Agent

The CloudWatch Agent is installed and configured on the EC2 instance to continuously monitor the application log file and send log events securely to Amazon CloudWatch Logs.


<img width="1575" height="227" alt="CloudWatchAgent" src="https://github.com/user-attachments/assets/d980bb88-e43f-4f9c-9977-45647f511639" />

---

## 📝 Log Generation

The Python application continuously generates INFO, WARNING, ERROR, and CRITICAL log events that simulate real-world application behavior for monitoring and alerting.


<img width="1022" height="522" alt="Log genration" src="https://github.com/user-attachments/assets/011fb3bc-cfa2-4bb2-a55b-d5f94903bcd8" />

---

## 📂 CloudWatch Log Group

Application logs are collected inside a dedicated CloudWatch Log Group, providing centralized log storage and enabling further analysis and monitoring.


<img width="1910" height="985" alt="CloudWatch LogGroup" src="https://github.com/user-attachments/assets/44824175-5647-4d22-989d-47a60b2c6e1a" />

---

## 📄 CloudWatch Log Streams

Each EC2 instance writes logs into CloudWatch Log Streams, allowing detailed inspection of incoming application events in real time.


<img width="1582" height="926" alt="Log Streams" src="https://github.com/user-attachments/assets/896188ef-64d6-409f-84ab-47f2bf9551c6" />

---

## 🎯 Metric Filter – Error Logs

A Metric Filter is configured to detect ERROR log entries and convert them into a custom CloudWatch metric for automated monitoring.


<img width="1907" height="917" alt="Metric Filter (1)" src="https://github.com/user-attachments/assets/34bbeb3e-2572-424f-a910-f82ae51251bf" />

---

## 🎯 Metric Filter – Warning & Critical Logs

Additional Metric Filters capture WARNING and CRITICAL log events, enabling independent monitoring of different log severity levels.


<img width="1481" height="985" alt="Metric Filter (2)" src="https://github.com/user-attachments/assets/209c5744-839b-4d7c-8fa9-d1b1b57f0976" />

---

## 📈 CloudWatch Metrics

Custom CloudWatch Metrics visualize the number of detected log events over time, helping administrators monitor application health.

<img width="1586" height="816" alt="Metric Graph(1)" src="https://github.com/user-attachments/assets/8c737a2b-377e-4651-93bf-801984bbcdc0" />

<img width="1586" height="816" alt="Metric Graph(1)" src="https://github.com/user-attachments/assets/9a5651ca-39bc-4389-a408-c5eb22eddfdf" />

---


## 🚨 Application Error Alarm

CloudWatch Alarm configured to monitor ERROR metrics. When the defined threshold is exceeded, the alarm changes state and initiates an SNS notification.


<img width="1595" height="847" alt="ApplicationErrorAlarm" src="https://github.com/user-attachments/assets/ae8dc144-ca62-4b3a-ac52-1218623f39ca" />

---

## 🚨 Application Warning Alarm

CloudWatch Alarm monitoring WARNING metrics to notify administrators whenever excessive warning events occur.

<img width="1592" height="866" alt="ApplicationWarningalarm" src="https://github.com/user-attachments/assets/164000ef-f6d2-4fa2-905b-10331be5d3ea" />

---

## 🚨 Application Critical Alarm

CloudWatch Alarm configured for CRITICAL application events. This alarm provides immediate notification whenever critical failures are detected.


<img width="1592" height="822" alt="ApplicationCriticalAlarm" src="https://github.com/user-attachments/assets/b5fb23bd-445d-41d9-9b91-01306da8741d" />

---

## 📧 Amazon SNS Subscription

Amazon SNS is configured to deliver alarm notifications through email. The subscription confirms successful integration between CloudWatch and SNS.


<img width="1562" height="667" alt="SNS Subscription" src="https://github.com/user-attachments/assets/accd4669-2e50-4be7-90d8-f53a0984d423" />

---

## 📩 Email Notification – Warning Alarm

Email notification received when the Warning Alarm enters the ALARM state, confirming that SNS notifications are working correctly.


<img width="1917" height="1022" alt="Email (Warning-Alarm)" src="https://github.com/user-attachments/assets/5c1affef-d41f-4802-aa2d-909e166f6fac" />

---

## 📩 Email Notification – Error Alarm

Email notification generated after the Error Alarm threshold is exceeded.


<img width="1917" height="1027" alt="Email (Error-Alarm)" src="https://github.com/user-attachments/assets/001dbfd2-6643-4e93-870c-cf51d1ae2233" />

---

## 📩 Email Notification – Critical Alarm

Critical alert email generated immediately after the Critical Alarm enters the ALARM state, demonstrating successful end-to-end monitoring and alerting.


<img width="1917" height="1027" alt="Email (Critical-Alarm)" src="https://github.com/user-attachments/assets/45cf557d-b01a-4f70-b469-3f465a041606" />

---
# ⚙️ AWS Services Used

This project leverages multiple AWS services to build a complete cloud monitoring and alerting solution.

| AWS Service | Purpose |
|------------|---------|
| Amazon EC2 | Hosts the Python application and CloudWatch Agent |
| Amazon CloudWatch Logs | Collects and stores application logs |
| CloudWatch Agent | Sends log files from EC2 to CloudWatch |
| CloudWatch Metric Filters | Converts log patterns into custom metrics |
| CloudWatch Metrics | Tracks ERROR, WARNING, and CRITICAL events |
| CloudWatch Alarms | Monitors metrics and triggers alerts |
| Amazon SNS | Sends email notifications when alarms are triggered |

---

# 🔄 Monitoring Workflow

The monitoring system follows an automated workflow to detect application issues and notify administrators.

```
Python Application
        │
        ▼
Generates Application Logs
        │
        ▼
CloudWatch Agent
        │
        ▼
CloudWatch Log Group
        │
        ▼
Metric Filters
        │
        ▼
Custom CloudWatch Metrics
        │
        ▼
CloudWatch Alarms
        │
        ▼
Amazon SNS
        │
        ▼
Email Notifications
```

---

# 📂 Project Structure

```text
aws-monitoring-alerting-system/
│
├── app.py
├── logs/
│   └── application.log
├── cloudwatch-config.json
├── screenshots/
├── README.md
└── LICENSE
```

---

# 📜 Key Components

### Python Log Generator

The Python application continuously generates different types of log events including:

- INFO
- WARNING
- ERROR
- CRITICAL

These logs simulate real-world application events and serve as the data source for CloudWatch monitoring.

---

### CloudWatch Agent

The CloudWatch Agent monitors the application log file in real time and forwards every new log event to Amazon CloudWatch Logs.

---

### CloudWatch Logs

CloudWatch Logs acts as the centralized repository for storing application logs generated by the EC2 instance.

---

### Metric Filters

Metric Filters analyze incoming log events and convert matching log patterns into custom CloudWatch Metrics.

Examples include:

- ERROR
- WARNING
- CRITICAL

---

### CloudWatch Metrics

Custom metrics provide a numerical representation of application events over time.

Metrics created include:

- ApplicationErrorCount
- ApplicationWarningCount
- ApplicationCriticalCount

---

### CloudWatch Alarms

CloudWatch Alarms continuously evaluate the custom metrics against predefined thresholds.

Whenever a threshold is exceeded, the alarm changes its state from **OK** to **ALARM**.

---

### Amazon SNS

Amazon Simple Notification Service distributes alarm notifications through email, ensuring administrators receive alerts immediately.

---

# 🧪 Testing

The project was tested using multiple log severity levels to verify the complete monitoring pipeline.

### Test Scenarios

✅ INFO Log Generated

✅ WARNING Log Generated

✅ ERROR Log Generated

✅ CRITICAL Log Generated

✅ Log Successfully Sent to CloudWatch

✅ Metric Filter Detected Log Pattern

✅ Custom Metric Updated

✅ CloudWatch Alarm Triggered

✅ SNS Notification Delivered

✅ Email Received Successfully

---

# 🔒 Security Considerations

The project follows AWS security best practices, including:

- IAM permissions for CloudWatch Agent
- Secure EC2 instance configuration
- Controlled access through Security Groups
- CloudWatch Agent configuration with least privilege
- Secure SNS topic subscription
- Centralized logging for easier auditing

---

# 📈 Project Highlights

- Automated log monitoring
- Real-time alert generation
- Cloud-native monitoring solution
- End-to-end observability
- Infrastructure hosted on AWS
- Event-driven notification system
- Modular and scalable architecture

---

# 🚀 Future Enhancements

Possible improvements for future versions include:

- Integration with AWS Lambda
- Slack Notifications
- Microsoft Teams Alerts
- SMS Notifications
- AWS EventBridge Integration
- Grafana Dashboard
- Prometheus Monitoring
- Auto Scaling Monitoring
- CPU and Memory Monitoring
- Disk Space Alerts
- Custom CloudWatch Dashboard Widgets
- Terraform Automation
- CloudFormation Deployment
- CI/CD Pipeline Integration
- Multi-Instance Monitoring
- Log Retention Policies
- Automated Incident Reporting


# 💡 Project Outcomes

After completing this project, the monitoring system successfully achieved the following objectives:

- Real-time log collection
- Automated log analysis
- Custom metric creation
- Alarm generation
- Instant email notifications
- Centralized cloud monitoring
- Improved application observability

---

# 🚀 Deployment Environment

The project was deployed using:

- Amazon EC2
- Ubuntu Linux
- Python
- CloudWatch Agent
- Amazon CloudWatch
- Amazon SNS


---


# 🙏 Acknowledgements

Special thanks to:

- Amazon Web Services
- Python Logging Library
- CloudWatch Documentation
- Open Source Community

for providing the tools and documentation that made this project possible.

---


<p align="center">

## 🚀 Built with Python, AWS CloudWatch, Amazon EC2, Amazon SNS, and Cloud Monitoring Best Practices


</p>
