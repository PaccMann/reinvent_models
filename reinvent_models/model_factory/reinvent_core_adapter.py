from reinvent_models.model_factory.enums.model_mode_enum import ModelModeEnum
from reinvent_models.model_factory.generative_model_base import GenerativeModelBase
from reinvent_models.reinvent_core.models.model import Model


class ReinventCoreAdapter(GenerativeModelBase):
    def __init__(self, path_to_file: str, mode: str):
        self.generative_model = Model.load_from_file(path_to_file, mode)
        self.vocabulary = self.generative_model.vocabulary
        self.tokenizer = self.generative_model.tokenizer
        self.max_sequence_length = self.generative_model.max_sequence_length
        self.network = self.generative_model.network
        # self._nll_loss =  self._reinvent_model._nll_loss

    def save_to_file(self, path):
        self.generative_model.save(path)

    def likelihood(self, sequences):
        return self.generative_model.likelihood(sequences)

    def sample(self, num, batch_size):
        return self.generative_model.sample_smiles(num, batch_size)

    def get_network_parameters(self):
        return self.generative_model.get_network_parameters()

    def get_vocabulary(self):
        return self.vocabulary
