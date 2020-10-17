

from mongo_setup import global_init
from patients import Patients
from services.package_service import PackageService


def main():
    global_init('curae_domo')


if __name__ == '__main__':
    main()
