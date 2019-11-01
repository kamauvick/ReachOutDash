import graphene
from graphene_django import DjangoObjectType

from .models import Chv, Patient, Emergencies, Location


class ChvType(DjangoObjectType):
    class Meta:
        model = Chv


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient


class EmergencyType(DjangoObjectType):
    class Meta:
        model = Emergencies


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class Query(graphene.ObjectType):
    chvs = graphene.List(ChvType)
    patients = graphene.List(PatientType)
    emergencies = graphene.List(EmergencyType)
    locations = graphene.List(LocationType)

    def resolve_chvs(self, info, **kwargs):
        return Chv.objects.all()

    def resolve_patients(self, info, **kwargs):
        return Patient.objects.all()

    def resolve_emergencies(self, info, **kwargs):
        return Emergencies.objects.all()

    def resolve_locations(self, info, **kwargs):
        return Location.objects.all()


schema = graphene.Schema(query=Query, subscription=Query)
