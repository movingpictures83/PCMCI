import rpy2
import rpy2.robjects as robjects
import numpy
from tigramite.pcmci import PCMCI
from tigramite.independence_tests import ParCorr
import tigramite.data_processing as pp
numpy.random.seed(42)

class PCMCIPlugin:
     def input(self, inputfile):
        self.links_coeffs = {}
        infile = open(inputfile, 'r')
        for line in infile:
           contents = line.split('\t')
           var = int(contents[0])
           driver = int(contents[1])
           lag = int(contents[2])
           coeff = float(contents[3])
           if (not var in self.links_coeffs):
              self.links_coeffs[var] = []
           self.links_coeffs[var].append(((driver, lag), coeff))

     def run(self):
        data, _ = pp.var_process(self.links_coeffs, T=1000)
        dataframe = pp.DataFrame(data)
        cond_ind_test = ParCorr()
        self.pcmciobj = PCMCI(dataframe=dataframe, cond_ind_test=cond_ind_test)
        self.results = self.pcmciobj.run_pcmci(tau_max=2, pc_alpha=None)

     def output(self, outputfile):
        self.pcmciobj.print_significant_links(p_matrix=self.results['p_matrix'],
                                       val_matrix=self.results['val_matrix'],
                                       alpha_level=0.05)
