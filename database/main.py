

from mongo_setup import global_init
from patients import Patients
from services.package_service import PackageService


def main():
    global_init('curae_domo')
    p = Patients()
    p.name = "Karl"
    p.address = "Berlin"
    p.phone = "00000000"
    p.care_level = "high"
    p.caretaker = "Alex"
    p.save()


if __name__ == '__main__':
    main()
