# Useful things!
from rest_framework import serializers
# MetaData-specific things
from olc_webportalv2.metadata.models import SequenceData, OLNID


class SequenceDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SequenceData
        fields = ('id', 'seqid', 'quality', 'genus', 'species', 'serotype', 'mlst', 'rmlst')


class SeqIDListingField(serializers.RelatedField):
    def to_representation(self, value):
        return '{}: {}'.format(value.seqid, value.quality)


class OLNSerializer(serializers.ModelSerializer):
    seqids = SeqIDListingField(many=True, read_only=True)

    class Meta:
        model = OLNID
        fields = ('olnid', 'seqids')
