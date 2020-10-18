from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo

app = Flask(__name__)
CORS(app)

# app.config['MONGO_DBNAME'] = 'curae_domo'
# app.config['MONGO_URI'] = \
#     'mongodb+srv://admin:admin@curae-domo.8k5nb.mongodb.net/curae_domo?retryWrites=true&w=majority'
#
# mongo = pymongo(app)

try:
    mongo = pymongo.MongoClient(
        host = "localhost",
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.curae_domo
    mongo.server_info()
except:
    print("ERROR Cannot connect to DB")

@app.route('/Patients', methods=['POST'])
def add_patients():
    patients = db.patients

    name = request.json['name']
    address = request.json['address']
    phone = request.json['phone']
    care_level = request.json['care_level']
    caretaker = request.json['caretaker']
    patient_vitals = request.json['patient_vitals']
    meds = request.json['meds']

    patients_id = patients.insert({
        'name': name,
        'address': address,
        'phone': phone,
        'care_level': care_level,
        'caretaker': caretaker,
        'patient_vitals': patient_vitals,
        'meds': meds
    })
    new_patients = patients.find_one({'_id': patients_id})

    output = {'name': new_patients['name'],
              'address': new_patients['address'],
              'phone': new_patients['phone'],
              'care_level': new_patients['care_level'],
              'caretaker': new_patients['caretaker'],
              'patient_vitals': new_patients['patient_vitals'],
              'meds': new_patients['meds'],
              }
    return jsonify({'result': output})

@app.route('/getAllPatients', methods=['GET'])
def get_all_patients():
    patients = db.patients
    output = []

    for q in patients.find():
        output.append({'name': q['name'],
                       'address': q['address'],
                       'phone': q['phone'],
                       'care_level': q['care_level'],
                       'caretaker': q['caretaker'],
                       'patient_vitals': q['patient_vitals'],
                       'meds': q['meds']
                       })

    return jsonify({'result': output})

#
# @app.route('/caretakers', methods=['POST'])
# def add_caretakers():
#     caretakers = mongo.db.caretakers
#
#     caretakerID = request.json['caretakerID']
#     name = request.json['name']
#     address = request.json['address']
#     phone = request.json['phone']
#     patients = request.json['patients']
#     doctors = request.json['doctors']
#
#     caretakers_id = caretakers.insert({
#         'caretakerID': caretakerID,
#         'name': name,
#         'address': address,
#         'phone': phone,
#         'patients': patients,
#         'doctors': doctors,
#     })
#     new_caretakers = caretakers.find_one({'_id': caretakers_id})
#
#     output = {
#         'caretakerID': new_caretakers['caretakerID'],
#         'name': new_caretakers['name'],
#         'address': new_caretakers['address'],
#         'phone': new_caretakers['phone'],
#         'patients': new_caretakers['patients'],
#         'doctors': new_caretakers['doctors']
#     }
#
#     return jsonify({'result': output})
#
#
# @app.route('/volunteers', methods=['POST'])
# def add_volunteers():
#     volunteers = mongo.db.volunteers
#
#     name = request.json['name']
#     phone = request.json['phone']
#     booking_time = request.json['booking_time']
#
#     volunteers_id = volunteers.insert({
#         'name': name,
#         'phone': phone,
#         'booking_time': booking_time
#     })
#     new_volunteers = volunteers.find_one({'_id': volunteers_id})
#
#     output = {'name': new_volunteers['name'],
#               'phone': new_volunteers['phone'],
#               'booking_time': new_volunteers['booking_time'],
#               }
#     return jsonify({'result': output})
#
#
#
# @app.route('/caretakers', methods=['GET'])
# def get_all_caretakers():
#     caretakers = mongo.db.caretakers
#
#     output = []
#
#     for q in caretakers.find():
#         output.append({'caretaker_id': q['caretaker_id'],
#                        'name': q['name'],
#                        'address': q['address'],
#                        'phone': q['phone'],
#                        'patients': q['patients'],
#                        'doctors': q['doctors']
#                        })
#
#     return jsonify({'result': output})
#
#
# @app.route('/volunteers', methods=['GET'])
# def get_all_caretakers():
#     volunteers = mongo.db.volunteers
#
#     output = []
#
#     for q in volunteers.find():
#         output.append({'name': q['name'],
#                        'phone': q['phone'],
#                        'booking_time': q['booking_time']
#                        })
#
#     return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
