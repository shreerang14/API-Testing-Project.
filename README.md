# API Testing Project

## 📌 Overview
This project demonstrates **API testing using Postman, Python (Requests + PyTest), and SQLite** with integration into a **CI/CD pipeline (GitHub Actions)**.  
It validates RESTful endpoints, checks payload structures, and performs data integrity checks in a database.

## 🛠️ Tech Stack
- **Postman** → API test collections (status code, payload validation)
- **Python + PyTest** → Automated API regression testing
- **Requests library** → HTTP calls
- **SQLite** → Store & validate API response data
- **GitHub Actions** → CI/CD pipeline to run tests on each push

## 🚀 Features
- Automated Postman tests (`postman_collection.json`)
- Python tests for:
  - ✅ API status code validation
  - ✅ Payload structure validation
  - ✅ Database integrity validation with SQL
  - ✅ Parameterized testing with JSON data
- End-to-end test pipeline running in GitHub Actions

## 📂 Project Structure
