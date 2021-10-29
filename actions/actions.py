from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database.dao import Dao

import asyncio

class ActionTampilFasilitasMinatBakat(Action):

    def name(self) -> Text:
        return "action_tampil_fasilitas_minat_bakat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        bidang_minat = str(next(tracker.get_latest_entity_values("bidang_minat"), None)).lower()
        message = ""

        if bidang_minat == "olahraga":
            message = "Fasilitas di bidang olahraga berupa lapangan olahraga."
        elif bidang_minat == "bem" or bidang_minat == "badan eksekutif mahasiswa" or bidang_minat == "hima" or bidang_minat == "himpunan mahasiswa" or bidang_minat == "ukm" or bidang_minat == "unit kegiatan mahasiswa":
            message = "Fasilitas di BEM, HIMA, dan Unit Kegiatan Mahasiswa berupa ruang kegiatan dan anggaran."
        elif bidang_minat == "kewirausahaan":
            message = "Fasilitas di bidang kewirausahaan berupa pelatihan karya tulis dan PKM."

        dispatcher.utter_message(text=message)

        return []

class ActionTampilPlatformSurvei(Action):

    def name(self) -> Text:
        return "action_tampil_platform_survei"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        jenis_survei = str(next(tracker.get_latest_entity_values("jenis_survei"), None)).lower()
        message = ""

        if jenis_survei == "kemahasiswaan":
            message = "Survei layanan kemahasiswaan dapat diakses di web cdc.unsri.ac.id."
        elif jenis_survei == "akademik":
            message = "Survei layanan akademik dapat diakses di web lp3mp.unsri.ac.id"

        dispatcher.utter_message(text=message)

        return []

class ActionTampilDefinisiSaranaAkademik(Action):
    dao = Dao()

    def name(self) -> Text:
        return "action_tampil_definisi_sarana_akademik"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sarana_akademik = str(next(tracker.get_latest_entity_values("sarana_akademik"), None)).lower()
        message = self.dao.get_academic_facil_desc(sarana_akademik)

        dispatcher.utter_message(text=message)

        return []

class ActionTampilJadwalSaranaAkademik(Action):
    dao = Dao()

    def name(self) -> Text:
        return "action_tampil_jadwal_sarana_akademik"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sarana_akademik = str(next(tracker.get_latest_entity_values("sarana_akademik"), None)).lower()
        message = self.dao.get_academic_facil_schedule(sarana_akademik)

        dispatcher.utter_message(text=message)

        return []

class ActionTampilPakaianWisuda(Action):

    def name(self) -> Text:
        return "action_tampil_pakaian_wisuda"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pakaian_wisuda = str(next(tracker.get_latest_entity_values("pakaian_wisuda"), None)).lower()
        message = ""

        if pakaian_wisuda == "mahasiswa":
            message = "Mahasiswa peserta upacara wisuda Universitas Sriwijaya mengenakan pakaian wisuda berupa toga, topi wisuda, atribut atau kelengkapan lainnya yang ditetapkan."
        elif pakaian_wisuda == "anggota senat" or pakaian_wisuda == "senat":
            message = "Anggota senat Universitas Sriwijaya mengenakan pakaian wisuda berupa toga, topi wisuda, atribut atau kelengkapan lainnya yang ditetapkan."
        elif pakaian_wisuda == "panitia":
            message = "Panitia pelaksana wisuda mengenakan pakaian sipil lengkap atau jas warna gelap."
        elif pakaian_wisuda == "undangan":
            message = "Undangan mengenakan pakaian sipil lengkap atau pakaian nasional (menyesuaikan)."
        else:
            message = "Silahkan input ulang pertanyaan anda"

        dispatcher.utter_message(text=message)

        return []

class ActionTampilWaktuTempatWisuda(Action):

    def name(self) -> Text:
        return "action_tampil_waktu_tempat_wisuda"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        kata_tanya = str(next(tracker.get_latest_entity_values("kata_tanya"), None)).lower()
        print(kata_tanya)
        message = ""

        if kata_tanya == "Kapan" or kata_tanya == "kapan":
            message = "Wisuda dilaksanakan pada waktu yang ditetapkan dalam Kalender Akademik Universitas Sriwijaya. kalender_akademik_ta_2021_-_2022.pdf (unsrittomohon.ac.id)."
        elif kata_tanya == "Dimana" or kata_tanya == "dimana":
            message = "Tempat pelaksanaan wisuda adalah Auditorium Universitas Sriwijaya atau tempat lain yang ditetapkan dan Peserta wisuda menempati tempat yang ditetapkan oleh panitia wisuda."

        dispatcher.utter_message(text=message)

        return []

class ActionTampilKuantitasDokumenWisuda(Action):

    def name(self) -> Text:
        return "action_tampil_kuantitas_dokumen_wisuda"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        qty_dokumen_wisuda = str(next(tracker.get_latest_entity_values("qty_dokumen_wisuda"), None)).lower()
        print(qty_dokumen_wisuda)
        message = ""

        if qty_dokumen_wisuda == "ijazah terakhir" or qty_dokumen_wisuda == "ijazah":
            message = "Menyerahkan 1 (satu) lembar fotokopi ijazah terakhir"
        elif qty_dokumen_wisuda == "pengesahan tugas akhir":
            message = "Menyerahkan 1 (satu) lembar fotokopi pengesahan tugas akhir"
        elif qty_dokumen_wisuda == "bukti kelulusan ujian penguasaan bahasa inggris" or qty_dokumen_wisuda == "bukti kelulusan ujian bahasa" or qty_dokumen_wisuda == "bukti kelulusan ujian bahasa inggris":
            message = "Menyerahkan bukti lulus ujian penguasaan Bahasa Inggris yang diakui 1 (satu) lembar fotokopi yang telah dilegalisir"
        elif qty_dokumen_wisuda == "pasfoto":
            message = "Menyerahkan 4 (empat) lembar pasfoto terbaru hitam putih ukuran 3 x 4 cm (laki laki pakai jas, wanita pakai kebaya)"

        dispatcher.utter_message(text=message)

        return []

class ActionTampilSyaratPredikatProgram(Action):
    dao = Dao()

    def name(self) -> Text:
        return "action_tampil_syarat_predikat_program"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        predikat = str(next(tracker.get_latest_entity_values("predikat"), None)).lower()
        program = str(next(tracker.get_latest_entity_values("program"), None)).lower()
        
        reqs = self.dao.get_predicate_requirements(predikat, program)
        reqs = reqs.replace(r'\n', '\n')
        if reqs == "":
            message = "Tidak terdapat predikat "+ predikat + " untuk program " + program
        else:
            message = "Syarat untuk memperoleh predikat " + predikat + " untuk mahasiswa program " + program + " yaitu:\n" + reqs

        dispatcher.utter_message(text=message)

        return []