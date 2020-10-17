from typing import Optional, List

from patients import Patients


class PackageService:
    @classmethod
    def package_count(cls):
        return Patients.objects().count()

    @classmethod
    def find_package_by_name(cls, name):
        package = Patients.objects(name=name).first()
        return package


    @classmethod
    def popular_packages(cls, limit: int) -> List[Patients]:
        packages = Patients.objects()\
            .order_by('name')\
            .limit(limit)

        return list(packages)
