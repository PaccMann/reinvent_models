from reinvent_models.lib_invent.models.model import DecoratorModel
from reinvent_models.model_factory.enums.model_mode_enum import ModelModeEnum
from reinvent_models.model_factory.generative_model_base import GenerativeModelBase


class LibInventAdapter(GenerativeModelBase):

    def __init__(self, path_to_file: str, mode: str):
        self.generative_model = DecoratorModel.load_from_file(path_to_file, mode)
        self.vocabulary = self.generative_model.vocabulary
        self.max_sequence_length = self.generative_model.max_sequence_length
        self.network = self.generative_model.network

    def save_to_file(self, path):
        self.generative_model.save_to_file(path)

    def likelihood(self, scaffold_seqs, scaffold_seq_lengths, decoration_seqs, decoration_seq_lengths):
        return self.generative_model.likelihood(scaffold_seqs, scaffold_seq_lengths, decoration_seqs, decoration_seq_lengths)

    def sample(self, scaffold_seqs, scaffold_seq_lengths):
        return self.generative_model.sample_decorations(scaffold_seqs, scaffold_seq_lengths)

    def set_mode(self, mode: str):
        self.generative_model.set_mode(mode)

    def get_network_parameters(self):
        return self.generative_model.get_network_parameters()

    def get_vocabulary(self):
        return self.vocabulary
