from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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
        elif pakaian_wisuda == "anggota senat":
            message = "Anggota senat Universitas Sriwijaya mengenakan pakaian wisuda berupa toga, topi wisuda, atribut atau kelengkapan lainnya yang ditetapkan."
        elif pakaian_wisuda == "panitia":
            message = "Panitia pelaksana wisuda mengenakan pakaian sipil lengkap atau jas warna gelap."
        elif pakaian_wisuda == "undangan":
            message = "Undangan mengenakan pakaian sipil lengkap atau pakaian nasional (menyesuaikan)."

        dispatcher.utter_message(text=message)

        return []
