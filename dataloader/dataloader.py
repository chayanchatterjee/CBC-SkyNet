"""Data Loader"""

# Imports
import numpy as np
import h5py

class DataLoader:
    """Data Loader class"""
    def __init__(self, num_det, dataset, n_test, n_samples):
        
        self.num_det = num_det
        self.dataset = dataset
        self.n_test = n_test
        self.n_samples = n_samples
    
#    @staticmethod
    def load_train_data(self, data_config):
        """Loads dataset from path"""
        # NSBH
        if(self.dataset == 'NSBH'):
            f1 = h5py.File(data_config.NSBH.path_train_1, 'r')
            f2 = h5py.File(data_config.NSBH.path_train_2, 'r')
            f3 = h5py.File(data_config.NSBH.path_train_3, 'r')
            f4 = h5py.File(data_config.NSBH.path_train_4, 'r')
            
            h1_real_52k = abs(f1['h1_snr_series'][()] )
            l1_real_52k = abs(f1['l1_snr_series'][()] )
            v1_real_52k = abs(f1['v1_snr_series'][()] )
        
            h1_real_30k = abs(f2['h1_snr_series'][()] )
            l1_real_30k = abs(f2['l1_snr_series'][()] )
            v1_real_30k = abs(f2['v1_snr_series'][()] )
            
            h1_real_12k = abs(f3['h1_snr_series'][()] )
            l1_real_12k = abs(f3['l1_snr_series'][()] )
            v1_real_12k = abs(f3['v1_snr_series'][()] )
        
            h1_real_6k = abs(f4['h1_snr_series'][()] )
            l1_real_6k = abs(f4['l1_snr_series'][()] )
            v1_real_6k = abs(f4['v1_snr_series'][()] )
            
            h1_real = np.concatenate([h1_real_52k, h1_real_30k, h1_real_12k, h1_real_6k], axis=0)
            l1_real = np.concatenate([l1_real_52k, l1_real_30k, l1_real_12k, l1_real_6k], axis=0)
            v1_real = np.concatenate([v1_real_52k, v1_real_30k, v1_real_12k, v1_real_6k], axis=0)
            
            h1_imag_52k = np.imag(f1['h1_snr_series'][()] )
            l1_imag_52k = np.imag(f1['l1_snr_series'][()] )
            v1_imag_52k = np.imag(f1['v1_snr_series'][()] )
        
            h1_imag_30k = np.imag(f2['h1_snr_series'][()] )
            l1_imag_30k = np.imag(f2['l1_snr_series'][()] )
            v1_imag_30k = np.imag(f2['v1_snr_series'][()] )
        
            h1_imag_12k = np.imag(f3['h1_snr_series'][()] )
            l1_imag_12k = np.imag(f3['l1_snr_series'][()] )
            v1_imag_12k = np.imag(f3['v1_snr_series'][()] )
        
            h1_imag_6k = np.imag(f4['h1_snr_series'][()] )
            l1_imag_6k = np.imag(f4['l1_snr_series'][()] )
            v1_imag_6k = np.imag(f4['v1_snr_series'][()] )
            
            h1_imag = np.concatenate([h1_imag_52k, h1_imag_30k, h1_imag_12k, h1_imag_6k], axis=0)
            l1_imag = np.concatenate([l1_imag_52k, l1_imag_30k, l1_imag_12k, l1_imag_6k], axis=0)
            v1_imag = np.concatenate([v1_imag_52k, v1_imag_30k, v1_imag_12k, v1_imag_6k], axis=0)
            
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            
        # BBH
        elif(self.dataset == 'BBH'):
            f1 = h5py.File(data_config.BBH.path_train, 'r')

            h1_real = abs(f1['h1_snr_series'][0:100000][()] )
            l1_real = abs(f1['l1_snr_series'][0:100000][()] )
            v1_real = abs(f1['v1_snr_series'][0:100000][()] )

            h1_imag = np.imag(f1['h1_snr_series'][0:100000][()] )
            l1_imag = np.imag(f1['l1_snr_series'][0:100000][()] )
            v1_imag = np.imag(f1['v1_snr_series'][0:100000][()] )
    
            f1.close()

        h1_real = h1_real[:,:,None]
        l1_real = l1_real[:,:,None]
        v1_real = v1_real[:,:,None]

        h1_imag = h1_imag[:,:,None]
        l1_imag = l1_imag[:,:,None]
        v1_imag = v1_imag[:,:,None]
        
        if(self.num_det == 3):
            X_train_real = np.concatenate((h1_real, l1_real, v1_real), axis=2)
            X_train_imag = np.concatenate((h1_imag, l1_imag, v1_imag), axis=2)
        
        elif(self.num_det == 2):
            X_train_real = np.concatenate((h1_real, l1_real), axis=2)
            X_train_imag = np.concatenate((h1_imag, l1_imag), axis=2)
        
        return X_train_real, X_train_imag
    
#    @staticmethod
    def load_train_parameters(self, data_config):
        """Loads train parameters from path"""
        #NSBH
        if(self.dataset == 'NSBH'):
            f1 = h5py.File(data_config.NSBH.path_train_1, 'r')
            f2 = h5py.File(data_config.NSBH.path_train_2, 'r')
            f3 = h5py.File(data_config.NSBH.path_train_3, 'r')
            f4 = h5py.File(data_config.NSBH.path_train_4, 'r')
        
            ra_52k = 2.0*np.pi*f1['ra'][()]
            dec_52k = np.arcsin(1.0-2.0*f1['dec'][()])
#            dec_52k = f1['dec'][()]
            ra_30k = 2.0*np.pi*(f2['ra'][0:30000][()])
            dec_30k = np.arcsin(1.0-2.0*f2['dec'][0:30000][()])
#            dec_30k = f2['dec'][0:30000][()]
            ra_12k = 2.0*np.pi*(f3['ra'][()])
            dec_12k = np.arcsin(1.0-2.0*f3['dec'][()])
#            dec_12k = f3['dec'][()]
            ra_6k = 2.0*np.pi*(f4['ra'][()])
            dec_6k = np.arcsin(1.0-2.0*f4['dec'][()])
#            dec_6k = f4['dec'][()]
        
            ra = np.concatenate([ra_52k, ra_30k, ra_12k, ra_6k])
            dec = np.concatenate([dec_52k, dec_30k, dec_12k, dec_6k])
            
        
            f1.close()
            f2.close()
            f3.close()
            f4.close()
        
        #BBH
        elif(self.dataset == 'BBH'):
            f1 = h5py.File(data_config.BBH.path_train, 'r')

            ra = 2.0*np.pi*f1['ra'][0:100000][()]
            dec = np.arcsin(1.0-2.0*f1['dec'][0:100000][()])
#            dec = f1['dec'][0:100000][()]
        
            f1.close()
        
        ra = ra[:,None]
        dec = dec[:,None]

        y_train = np.concatenate((ra, dec), axis=1)

        return y_train
    
#    @staticmethod
    def load_test_data(self, data_config):
        """Loads dataset from path"""
        #Get the HDF5 group
        #NSBH
        if(self.dataset == 'NSBH'):
            f_test = h5py.File(data_config.NSBH.path_test, 'r')
            
        elif(self.dataset == 'BBH'):
            f_test = h5py.File(data_config.BBH.path_test, 'r')
            
        group_test = f_test['omf_injection_snr_samples']
        
        data_h1_test = group_test['h1_snr']
        data_l1_test = group_test['l1_snr']
        data_v1_test = group_test['v1_snr']
        
        h1_test_real = np.zeros([self.n_test, self.n_samples])
        l1_test_real = np.zeros([self.n_test, self.n_samples])
        v1_test_real = np.zeros([self.n_test, self.n_samples])
        
        h1_test_imag = np.zeros([self.n_test, self.n_samples])
        l1_test_imag = np.zeros([self.n_test, self.n_samples])
        v1_test_imag = np.zeros([self.n_test, self.n_samples])
        
        for i in range(self.n_test):
            h1_test_real[i] = abs(data_h1_test[str(i)][()][1840:2250] )
            l1_test_real[i] = abs(data_l1_test[str(i)][()][1840:2250] )
            v1_test_real[i] = abs(data_v1_test[str(i)][()][1840:2250] )
    
            h1_test_imag[i] = np.imag(data_h1_test[str(i)][()][1840:2250] )
            l1_test_imag[i] = np.imag(data_l1_test[str(i)][()][1840:2250] )
            v1_test_imag[i] = np.imag(data_v1_test[str(i)][()][1840:2250] )
        
        f_test.close()
        
        h1_test_real = h1_test_real[:,:,None]
        l1_test_real = l1_test_real[:,:,None]
        v1_test_real = v1_test_real[:,:,None]
    
        h1_test_imag = h1_test_imag[:,:,None]
        l1_test_imag = l1_test_imag[:,:,None]
        v1_test_imag = v1_test_imag[:,:,None]
        
        if(self.num_det == 3):
            
            X_test_real = np.concatenate((h1_test_real, l1_test_real, v1_test_real), axis=2)
            X_test_imag = np.concatenate((h1_test_imag, l1_test_imag, v1_test_imag), axis=2)
            
        elif(self.num_det == 2):
            
            X_test_real = np.concatenate((h1_test_real, l1_test_real), axis=2)
            X_test_imag = np.concatenate((h1_test_imag, l1_test_imag), axis=2)
            
    
        return X_test_real, X_test_imag

           
#    @staticmethod
    def load_test_parameters(self, data_config):
        """Loads train parameters from path"""
        if(self.dataset == 'NSBH'):
            
            f_test = h5py.File(data_config.NSBH.path_test, 'r')
            
        elif(self.dataset == 'BBH'):
            
            f_test = h5py.File(data_config.BBH.path_test, 'r')
            
        data_ra = f_test['ra'][()]
        data_dec = f_test['dec'][()]

        f_test.close()

        ra_test = 2.0*np.pi*data_ra
        dec_test = np.arcsin(1.0 - 2.0*data_dec)
#        dec_test = data_dec
        
        ra_test = ra_test[:,None]
        dec_test = dec_test[:,None]

        y_test = np.concatenate((ra_test, dec_test), axis=1)

        return y_test, ra_test, dec_test
    
    
#    @staticmethod
    def load_3_det_samples(self, data_config, X_real, X_imag, y, num_samples, data):
        """Loads 3 det samples and parameters from path"""
        if(self.dataset == 'NSBH'):
            
            if(data == 'train'):
                f1 = h5py.File(data_config.NSBH.path_train_1, 'r')
                f2 = h5py.File(data_config.NSBH.path_train_2, 'r')
                f3 = h5py.File(data_config.NSBH.path_train_3, 'r')
                f4 = h5py.File(data_config.NSBH.path_train_4, 'r')            
                
        
                h1_snr_1 = f1['H1_SNR'][()]
                h1_snr_2 = f2['H1_SNR'][0:30000][()]
                h1_snr_3 = f3['H1_SNR'][()]
                h1_snr_4 = f4['H1_SNR'][()]            
                

                h1_snr = np.concatenate([h1_snr_1, h1_snr_2, h1_snr_3, h1_snr_4])
        
                l1_snr_1 = f1['L1_SNR'][()]
                l1_snr_2 = f2['L1_SNR'][0:30000][()]
                l1_snr_3 = f3['L1_SNR'][()]
                l1_snr_4 = f4['L1_SNR'][()]            
                

                l1_snr = np.concatenate([l1_snr_1, l1_snr_2, l1_snr_3, l1_snr_4])

                v1_snr_1 = f1['V1_SNR'][()]
                v1_snr_2 = f2['V1_SNR'][0:30000][()]
                v1_snr_3 = f3['V1_SNR'][()]
                v1_snr_4 = f4['V1_SNR'][()]            
                

                v1_snr = np.concatenate([v1_snr_1, v1_snr_2, v1_snr_3, v1_snr_4])
        
                h1 = h1_snr > 4
                l1 = l1_snr > 4
                v1 = v1_snr > 4
            
                ra_1 = 2.0*np.pi*f1['ra'][()]
                ra_2 = 2.0*np.pi*f2['ra'][0:30000][()]
                ra_3 = 2.0*np.pi*f3['ra'][()]
                ra_4 = 2.0*np.pi*f4['ra'][()]
                
                dec_1 = np.arcsin(1.0-2.0*f1['dec'][()])
                dec_2 = np.arcsin(1.0-2.0*f2['dec'][0:30000][()])
                dec_3 = np.arcsin(1.0-2.0*f3['dec'][()])
                dec_4 = np.arcsin(1.0-2.0*f4['dec'][()])

#                dec_1 = f1['dec'][()]
#                dec_2 = f2['dec'][0:30000][()]
#                dec_3 = f3['dec'][()]
#                dec_4 = f4['dec'][()]
            
                ra = np.concatenate([ra_1, ra_2, ra_3, ra_4])
                dec = np.concatenate([dec_1, dec_2, dec_3, dec_4])

    
                f1.close()
                f2.close()
                f3.close()
                f4.close()
            
            elif(data == 'test'):
                f_test = h5py.File(data_config.NSBH.path_test, 'r')
                h1_snr = f_test['H1_SNR'][()]
                l1_snr = f_test['L1_SNR'][()]
                v1_snr = f_test['V1_SNR'][()]
            
                h1 = h1_snr > 4
                l1 = l1_snr > 4
                v1 = v1_snr > 4
            
                ra = 2.0*np.pi*f_test['ra'][()]
                dec = np.arcsin(1.0-2.0*f_test['dec'][()])
#                dec = f_test['dec'][()]

                f_test.close()
                
        
        elif(self.dataset == 'BBH'):
            if(data == 'train'):
                f1 = h5py.File(data_config.BBH.path_train, 'r')
                
                h1_snr = f1['H1_SNR'][0:100000][()]
                l1_snr = f1['L1_SNR'][0:100000][()]
                v1_snr = f1['V1_SNR'][0:100000][()]
                
                h1 = h1_snr > 4
                l1 = l1_snr > 4
                v1 = v1_snr > 4
        
                ra = 2.0*np.pi*f1['ra'][0:100000][()]
                dec = np.arcsin(1.0-2.0*f1['dec'][0:100000][()])
#                dec = f1['dec'][()]
                
                f1.close()
                
            elif(data == 'test'):
                f1 = h5py.File(data_config.BBH.path_test, 'r')
                
                h1_snr = f1['H1_SNR'][()]
                l1_snr = f1['L1_SNR'][()]
                v1_snr = f1['V1_SNR'][()]
                
                h1 = h1_snr > 4
                l1 = l1_snr > 4
                v1 = v1_snr > 4
        
                ra = 2.0*np.pi*f1['ra'][()]
                dec = np.arcsin(1.0-2.0*f1['dec'][()])
#                dec = f1['dec'][()]
                
                f1.close()
        
        index = np.zeros(num_samples, dtype = bool)
        
        for i in range(num_samples):
            if(self.num_det == 3):
                if(h1[i] == True and l1[i] == True and v1[i] == True):
                    index[i] = True
                    
            elif(self.num_det == 2):
                if(h1[i] == True and l1[i] == True):
                    index[i] = True
                
        X_real = X_real[index == True]
        X_imag = X_imag[index == True]
        y = y[index == True]
        ra = ra[index == True]
        dec = dec[index == True]

        return X_real, X_imag, y, ra, dec
    

