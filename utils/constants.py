# These fields define which features comprise the flow ID
ARGUS_FLOW_ID = ['SrcAddr', 'Sport', 'DstAddr', 'Dport', 'Proto']

# These fields define which features comprise the flow feature vector
ARGUS_FIELDS = ['sTtl', 'dTtl', 'SrcPkts', 'DstPkts', 'SrcBytes', 'DstBytes', 'SrcLoad', 'DstLoad', 'Dir',
                'SIntPkt', 'DIntPkt', 'SIntPktAct', 'DIntPktAct', 'SIntPktIdl', 'DIntPktIdl', 'SrcJitter',
                'DstJitter', 'SrcJitAct', 'DstJitAct', 'State', 'sMaxPktSz', 'dMaxPktSz', 'sMinPktSz',
                'dMinPktSz', 'Dur', 'Rate', 'SrcRate', 'DstRate', 'RunTime', 'Mean', 'Sum', 'Min',
                'Max', 'Load', 'pSrcLoss', 'pDstLoss']

# Numeric encoding for states and direction, which are non-numeric discrete parameters
ARGUS_DIRECTIONS = {'->': 0, '?>': 1, '<-': 2, '<?': 3, '<->': 4, '<?>': 5, 'who': 6}

ARGUS_STATES = {'ACC': 12, 'DCE': 23, 'REQ': 9, 'URFIL': 17, 'RED': 8, 'CON': 2, 'URHPRO': 6,
                'ECO': 5, 'TXD': 15, 'ECR': 14, 'NNS': 16, 'SRC': 22, 'URF': 20, 'CLO': 19,
                'STA': 0, 'URN': 10, 'URO': 21, 'URH': 11, 'URNPRO': 24, 'RST': 1, 'URP': 7,
                'FIN': 3, 'INT': 4, 'NRS': 18, 'RSP': 13}
