from reinvent_models.link_invent.link_invent_model import LinkInventModel
from reinvent_models.model_factory.enums.model_mode_enum import ModelModeEnum
from reinvent_models.model_factory.generative_model_base import GenerativeModelBase


class LinkInventAdapter(GenerativeModelBase):

    def __init__(self, path_to_file: str, mode: str):
        self.generative_model = LinkInventModel.load_from_file(path_to_file, mode)
        self.vocabulary = self.generative_model.vocabulary
        self.max_sequence_length = self.generative_model.max_sequence_length
        self.network = self.generative_model.network

    def save_to_file(self, path):
        self.generative_model.save_to_file(path)

    def likelihood(self, warheads_seqs, warheads_seq_lengths, linker_seqs, linker_seq_lengths):
        return self.generative_model.likelihood(warheads_seqs, warheads_seq_lengths, linker_seqs, linker_seq_lengths)

    def sample(self, warheads_seqs, warheads_seq_lengths):
        return self.generative_model.sample(warheads_seqs, warheads_seq_lengths)

    def set_mode(self, mode: str):
        self.generative_model.set_mode(mode)

    def get_network_parameters(self):
        return self.generative_model.get_network_parameters()

    def get_vocabulary(self):
        return self.vocabulary
