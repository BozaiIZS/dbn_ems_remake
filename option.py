class Option:
    def __init__(self):

        self.wandb = False
        self.wandb_username = 'siyuan1098'

        # load
        self.folder_path = "./data"
        self.num_person = 4
        self.num_gesture = 12
        self.num_channel = 6
        self.num_row_perpage = 4165

        # ssa
        self.ssa_window_length=12
        self.ssa_save_length=1

        # slide window
        self.slidewindow_length = 60
        self.slidewindow_stride = 30

        # compare

        self.compare_valid_size = 0.2
        self.compare_test_size = 0.1
        self.compare_stratify = True
        self.compare_random_state = 23
        self.compare_shuffle = True
        self.compare_show_plots = False
        self.compare_bs = 64
        self.compare_inplace = True

        # xceptiontime

        self.xceptiontime_valid_size = 0.2
        self.xceptiontime_test_size = 0.1
        self.xceptiontime_stratify = True
        self.xceptiontime_random_state = 23
        self.xceptiontime_shuffle = True
        self.xceptiontime_show_plots = True
        self.xceptiontime_bs = 256
        self.xceptiontime_inplace = True

        # ominiscalecnn

        self.omniscalecnn_valid_size = 0.2
        self.omniscalecnn_test_size = 0.1
        self.omniscalecnn_stratify = True
        self.omniscalecnn_random_state = 23
        self.omniscalecnn_shuffle = True
        self.omniscalecnn_show_plots = False
        self.omniscalecnn_bs = 64
        self.omniscalecnn_inplace = True

        # rbm
        self.rbm_mode = 'bernoulli'  # bernoulli or gaussian RBM
        self.rbm_lr = 0.0001  # Learning rate for the CD algorithm
        self.rbm_epochs = 3000  # Number of iterations to run the algorithm for
        self.rbm_batch_size = 64
        self.rbm_k = 3
        self.rbm_optimizer = 'adam'
        self.rbm_beta_1 = 0.9
        self.rbm_beta_2 = 0.999
        self.rbm_epsilon = 1e-07
        self.rbm_savefile = None
        self.rbm_early_stopping_patience = 50
        self.rbm_stagnation = 0
        self.rbm_previous_loss_before_stagnation = 0
        self.rbm_progress = []
        self.rbm_gpu=True


        #dbn

        self.dbn_layers = [20,16]
        self.dbn_k = 3
        self.dbn_mode = 'bernoulli'
        self.dbn_savefile='./models/dbn_pretrained_model.pt'


        #dbn_last_layer
        self.dll_epoch=100
        self.dll_batch_size=32
        self.dll_learning_rate=0.001
        self.dll_loadfile='./models/dbn_pretrained_model.pt'
        self.dll_savefile='./models/dbn_trained_model.pt'

