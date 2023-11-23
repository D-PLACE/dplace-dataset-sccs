import pathlib

from pydplace import DatasetWithSocieties


class Dataset(DatasetWithSocieties):
    dir = pathlib.Path(__file__).parent
    id = "dplace-dataset-sccs"

    def local_makecldf(self, args):
        ehraf = {'SCCS' + row['SCCS ID']: (row['eHRAF ID'], row['eHRAF Name']) for row in self.etc_dir.read_csv('ehraf-ccr.csv', dicts=True) if row['SCCS ID'] != 'None'}
        for row in args.writer.objects['LanguageTable']:
            row['HRAF_ID'] = ehraf[row['ID']][0]
            row['HRAF_name_ID'] = '{} ({})'.format(ehraf[row['ID']][1], ehraf[row['ID']][0])

        args.writer.cldf.add_provenance(wasDerivedFrom={
            "rdf:about": "https://hraf.yale.edu/cross-cultural-concordance/",
            "rdf:type": "prov:Entity",
            "dc:created": "2020",
            "dc:title": "HRAF Cross Cultural Concordance",
            "dc:bibliographicCitation": "Ember et al. 2020. HRAF Cross Cultural Concordance."
        })

