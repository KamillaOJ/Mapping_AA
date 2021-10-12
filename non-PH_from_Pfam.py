import os, glob


pdb_PTB = "2YT8_1,2YT7_1,6DM4_2,3O17_2,3D8F_1,2E45_1,2YT1_1,6O5O_1,1NU2_1,3O2M_2,3H8D_2,1NTV_1,5LW1_3,6FUZ_1,2G01_2,6LNM_2,5YI7_1,5YI8_1,4DBB_1,6F5E_3,2NMB_1,2MYQ_1,1N3H_1,3F0W_1,3SUZ_1,3SV1_1,1SHC_1,2L1C_1,1AQC_1,2YSC_1,3D8D_1,2YSZ_1,3D8E_1,1OY2_1,3VUG_2,4JMH_2,5NQH_1,3VUH_2,3VUK_2,3VUI_2,4E73_2,2FPD_1,3VUL_2,2EJ8_1,6ITU_1,1WJ1_1,3OXI_2,5C5B_2,5C5B_1,6F7O_1,2FPF_1,2LSW_1,1WGU_1,4Z88_2,2ELA_1,2ELB_1,2DYQ_1,2FPE_1,3VUM_2,5UWS_4,2GMX_2,6OVF_1,2IDH_1,2OEI_1,4H8S_1,2EAM_1,1OQN_1,1TCE_1,4G1W_2,4XWX_1,5YQG_2,1X11_1,1M7E_1,1MIL_1,4HYS_2,1P3R_1,2Z0N_1,2LMR_1,3QYB_1,5NJK_1,2Q12_1,5NJJ_1,3PTG_2,3DXC_1,3QYE_1,1X45_1,1UKI_2,3DXE_1,1Y7N_1,3SO6_1,2Z0O_1,2KIV_1,2Q13_1,4NC6_1,3DXD_1,1UKH_2,2HO2_1,2YT0_1,2M38_1,2H96_2,5ZRY_1,4HYU_2,1DDM_1,1QG1_2,1U39_1,4IZY_2,3V3V_2,3VUD_2,6KMH_2,2KE7_1,1U3B_1,2ROZ_2,5CZI_2,1U37_1,4H39_2,1U38_1"
pdb_RANDB = "5UWW_2,6KFT_2,1K5G_2,5UWT_2,3UIO_4,5UWI_2,6CIT_2,4HAU_2,4HB2_2,4HAT_2,4HB3_2,4HB4_2,4HAX_3,4HAV_2,4HAW_2,3TJ3_2,4HB0_2,5DIF_2,1XKE_1,5DH9_2,4GMX_2,2CRF_1,6XJT_2,6XJU_2,6XJR_2,6XJS_2,5DHF_2,5DHA_2,4LQW_1,5UWJ_2,3UIP_4,5UWH_2,3UIN_4,5JLJ_2,5ZPU_2,2C1M_2,4GA0_1,6A38_2,2C1T_2,5DI9_2,6A3E_2,6A3C_2,6A3B_2,6A3A_2,4HAZ_2,4HAY_2,4GPT_2,2LAS_2,7L5E_2,4GA1_1,1UN0_2,5UWU_2,1RRP_2,5UWS_2,3OAN_1,5CLL_2,5YRO_2,6XJP_2,4L6E_1,6M6X_2,5CLQ_2,6X2M_2,6X2O_2,5YSU_2,6X2S_2,6X2U_2,5YST_2,6X2V_2,6X2W_2,6X2X_2,6X2Y_2,6X2R_2,6X2P_2,4WVF_2,5YTB_2,2EC1_1,5UWQ_2,1K5D_2,5UWR_2,5UWO_2,5UWP_2,2Y8G_1,3N7C_1,4I9Y_1,3M1I_2,5XZX_2,1Z5S_4,2Y8F_1,3WYF_2,4GA2_1"
pdb_EVH = "1TJ6_1,5N91_1,5ZZ9_1,5N9C_1,1CEE_2,2XQN_2,3RSE_8,6RCJ_1,6RCF_1,3CHW_3,2V8C_2,2PBD_3,6RD2_1,2PAV_3,2IYB_1,6XXR_1,7A5M_1,2OT0_2,1XOD_1,1I2H_1,1EVH_1,6V65_1,1USD_1,1USE_1,7AKI_1,1ZUK_2,4MY6_1,2IFS_1,3SYX_1,1QC6_1,2JP2_1,3CVF_1,1T84_1,5N9P_1,2FF3_2,6UHC_8,1I7A_1,2P8V_1,5NDU_1,2LNH_1,3M3N_2,5NCG_1,5NCF_1,5NEG_1,2A3Z_3,6XVT_1,1MKE_1,2VCP_2,2HO2_2,3CVE_1,1EJ5_1,5NCP_1,5ND0_1,1DDW_1,5NC7_1,1DDV_1,2K42_1,4CC7_2,4CC3_2,1EGX_1,4CC2_2,5NBF_1,5NAJ_1,6V6F_1,5NC2_1,5NBX_1"
pdb_Dcp = "5JP4_1,2QKL_1,4B6H_1,5J3Q_1,5N2V_1,1Q67_1,6Y3Z_2,2QKM_1,5J3Y_1,5LOP_2,5LON_2,5KQ1_1,6AM0_2,5J3T_1,2LYD_1,5KQ4_1"

lPTB = []
PTB = []

lRanBD = []
RanBD = []

lEVH = []
EVH = []

lDcp = []
Dcp = []

lPTB.append(pdb_PTB.split(","))
lRanBD.append(pdb_RANDB.split(","))
lEVH.append(pdb_EVH.split(","))
lDcp.append(pdb_Dcp.split(","))



for ID in lPTB:
    for letter in ID:
        PTB.append(letter[0:4])

for ID in lRanBD:
    for letter in ID:
        RanBD.append(letter[0:4])
        
for ID in lEVH:
    for letter in ID:
        EVH.append(letter[0:4])

for ID in lDcp:
    for letter in ID:
        Dcp.append(letter[0:4])

PTB = ['2YT8', '2YT7', '6DM4', '3O17', '3D8F', '2E45', '2YT1', '6O5O', '1NU2',
       '3O2M', '3H8D', '1NTV', '5LW1', '6FUZ', '2G01', '6LNM', '5YI7', '5YI8',
       '4DBB', '6F5E', '2NMB', '2MYQ', '1N3H', '3F0W', '3SUZ', '3SV1', '1SHC',
       '2L1C', '1AQC', '2YSC', '3D8D', '2YSZ', '3D8E', '1OY2', '3VUG', '4JMH',
       '5NQH', '3VUH', '3VUK', '3VUI', '4E73', '2FPD', '3VUL', '2EJ8', '6ITU',
       '1WJ1', '3OXI', '5C5B', '5C5B', '6F7O', '2FPF', '2LSW', '1WGU', '4Z88',
       '2ELA', '2ELB', '2DYQ', '2FPE', '3VUM', '5UWS', '2GMX', '6OVF', '2IDH',
       '2OEI', '4H8S', '2EAM', '1OQN', '1TCE', '4G1W', '4XWX', '5YQG', '1X11',
       '1M7E', '1MIL', '4HYS', '1P3R', '2Z0N', '2LMR', '3QYB', '5NJK', '2Q12',
       '5NJJ', '3PTG', '3DXC', '3QYE', '1X45', '1UKI', '3DXE', '1Y7N', '3SO6',
       '2Z0O', '2KIV', '2Q13', '4NC6', '3DXD', '1UKH', '2HO2', '2YT0', '2M38',
       '2H96', '5ZRY', '4HYU', '1DDM', '1QG1', '1U39', '4IZY', '3V3V', '3VUD',
       '6KMH', '2KE7', '1U3B', '2ROZ', '5CZI', '1U37', '4H39', '1U38']

RanBD = ['5UWW', '6KFT', '1K5G', '5UWT', '3UIO', '5UWI', '6CIT', '4HAU', '4HB2',
         '4HAT', '4HB3', '4HB4', '4HAX', '4HAV', '4HAW', '3TJ3', '4HB0', '5DIF',
         '1XKE', '5DH9', '4GMX', '2CRF', '6XJT', '6XJU', '6XJR', '6XJS', '5DHF',
         '5DHA', '4LQW', '5UWJ', '3UIP', '5UWH', '3UIN', '5JLJ', '5ZPU', '2C1M',
         '4GA0', '6A38', '2C1T', '5DI9', '6A3E', '6A3C', '6A3B', '6A3A', '4HAZ',
         '4HAY', '4GPT', '2LAS', '7L5E', '4GA1', '1UN0', '5UWU', '1RRP', '5UWS',
         '3OAN', '5CLL', '5YRO', '6XJP', '4L6E', '6M6X', '5CLQ', '6X2M', '6X2O',
         '5YSU', '6X2S', '6X2U', '5YST', '6X2V', '6X2W', '6X2X', '6X2Y', '6X2R',
         '6X2P', '4WVF', '5YTB', '2EC1', '5UWQ', '1K5D', '5UWR', '5UWO', '5UWP',
         '2Y8G', '3N7C', '4I9Y', '3M1I', '5XZX', '1Z5S', '2Y8F', '3WYF', '4GA2']

EVH = ['1TJ6', '5N91', '5ZZ9', '5N9C', '1CEE', '2XQN', '3RSE', '6RCJ', '6RCF',
       '3CHW', '2V8C', '2PBD', '6RD2', '2PAV', '2IYB', '6XXR', '7A5M', '2OT0',
       '1XOD', '1I2H', '1EVH', '6V65', '1USD', '1USE', '7AKI', '1ZUK', '4MY6',
       '2IFS', '3SYX', '1QC6', '2JP2', '3CVF', '1T84', '5N9P', '2FF3', '6UHC',
       '1I7A', '2P8V', '5NDU', '2LNH', '3M3N', '5NCG', '5NCF', '5NEG', '2A3Z',
       '6XVT', '1MKE', '2VCP', '2HO2', '3CVE', '1EJ5', '5NCP', '5ND0', '1DDW',
       '5NC7', '1DDV', '2K42', '4CC7', '4CC3', '1EGX', '4CC2', '5NBF', '5NAJ',
       '6V6F', '5NC2', '5NBX']


PTBcath = ['1shcA00', '5c5bA02', '1ntvA00', '3d8eB00', '4h8sD02', '5c5bC02',
           '4xwxA00', '1x11A00', '2elbA02', '1nu2A00', '2nmbA00', '3dxdA00',
           '1p3rC00', '3d8eD00', '3suzA01', '1p3rA00', '4h8sB02', '1n3hA00',
           '3dxdC00', '3d8eA00', '1ddmA00', '5c5bB02', '2yt0A01', '2q13A02',
           '1wguA01', '2z0oA02', '3d8eC00', '1x11B00', '2m38A00', '4h8sC02',
           '5c5bD02', '4h8sA02', '1p3rB00', '3d8fD00', '3f0wA00', '2rozB00',
           '3d8dB00', '2ej8B00', '1m7eB00', '1wj1A01', '4dbbA00', '3d8fB00',
           '1aqcA00', '2elaA00', '3sv1B00', '3dxeC00', '3dxeA00', '1oqnB00',
           '1m7eC00', '2yszA01', '3so6A00', '2dyqA00', '1m7eA00', '3d8dA00',
           '2yt1A01', '2ej8A00', '3sv1A00', '2elaB00', '3dxcA00', '1aqcB00',
           '3d8fA00', '2l1cA00', '3d8fC00', '1oy2A00', '3dxcC00', '3sv1C00',
           '1oqnA00']

RanBDcath = ['4l6eA00', '1k5dB00', '5dh9B00', '1xkeA00', '1rrpD00', '2y8fA00',
             '3wyfB00', '4hb3B00', '5di9B00', '2ec1A00', '2y8fC00', '1rrpB00',
             '1k5gK00', '5dhaB00', '2y8fD00', '5cllD00', '4hawB00', '3wyfE00',
             '2y8fB00', '4hayB00', '4hauB00', '1k5dE00', '1k5gH00', '2crfA01',
             '5cllB00', '5dhfB00', '4hb0B00', '3oanA00', '5jljB00', '5clqB00',
             '1k5dK00', '5clqD00', '1k5gB00', '4hb2B00', '5difB00', '3n7cA00',
             '2y8gA00', '3m1iB00', '4havB00', '4hazB00', '4gmxB00', '1k5dH00',
             '1k5gE00', '4hb4B00', '4haxB00', '2y8gB00', '4hatB00', '3n7cB00',
             '4gptB00', '4wvfB00']

EVHcath = ['1xodB00', '1i7aD00', '1qc6A00', '2iybD00', '1i7aB00', '1evhA00',
           '1mkeA00', '2iybB00', '1xodA00', '2xqnM00', '1qc6B00', '1i2hA00',
           '1i7aA00', '2iybC00', '2iybA00', '1i7aC00', '1ddwA00', '4my6B00',
           '1egxA00', '1tj6B00', '4my6A00', '2ifsA00', '1tj6A00', '2p8vA00',
           '1ddvA00', '3syxA00', '2jp2A00']

Dcpcath = ['2qkmC00', '5kq1A00', '4b6hB00', '2qkmA00', '5j3tA00', '2qkmE00',
           '1q67B01', '2qkmG00', '4b6hA00', '5kq1D00', '1q67A01', '2qklA00',
           '5lopB01', '5kq4D00', '5j3yC00', '5j3yA00', '5j3qC00', '5jp4A00',
           '5j3qA00', '5lonB01', '2lydA00', '5kq4A00'] ###22


FakePH =  ['1shcA00', '5c5bA02', '1ntvA00', '3d8eB00', '4h8sD02', '5c5bC02',
           '4xwxA00', '1x11A00', '2elbA02', '1nu2A00', '2nmbA00', '3dxdA00',
           '1p3rC00', '3d8eD00', '3suzA01', '1p3rA00', '4h8sB02', '1n3hA00',
           '3dxdC00', '3d8eA00', '1ddmA00', '5c5bB02', '2yt0A01', '2q13A02',
           '1wguA01', '2z0oA02', '3d8eC00', '1x11B00', '2m38A00', '4h8sC02',
           '5c5bD02', '4h8sA02', '1p3rB00', '3d8fD00', '3f0wA00', '2rozB00',
           '3d8dB00', '2ej8B00', '1m7eB00', '1wj1A01', '4dbbA00', '3d8fB00',
           '1aqcA00', '2elaA00', '3sv1B00', '3dxeC00', '3dxeA00', '1oqnB00',
           '1m7eC00', '2yszA01', '3so6A00', '2dyqA00', '1m7eA00', '3d8dA00',
           '2yt1A01', '2ej8A00', '3sv1A00', '2elaB00', '3dxcA00', '1aqcB00',
           '3d8fA00', '2l1cA00', '3d8fC00', '1oy2A00', '3dxcC00', '3sv1C00',
           '1oqnA00', '4l6eA00', '1k5dB00', '5dh9B00', '1xkeA00', '1rrpD00',
           '2y8fA00', '3wyfB00', '4hb3B00', '5di9B00', '2ec1A00', '2y8fC00', 
           '1rrpB00', '1k5gK00', '5dhaB00', '2y8fD00', '5cllD00', '4hawB00',
           '3wyfE00', '2y8fB00', '4hayB00', '4hauB00', '1k5dE00', '1k5gH00',
           '2crfA01', '5cllB00', '5dhfB00', '4hb0B00', '3oanA00', '5jljB00', 
           '5clqB00', '1k5dK00', '5clqD00', '1k5gB00', '4hb2B00', '5difB00',
           '3n7cA00', '2y8gA00', '3m1iB00', '4havB00', '4hazB00', '4gmxB00',
           '1k5dH00', '1k5gE00', '4hb4B00', '4haxB00', '2y8gB00', '4hatB00', 
           '3n7cB00', '4gptB00', '4wvfB00', '1xodB00', '1i7aD00', '1qc6A00',
           '2iybD00', '1i7aB00', '1evhA00', '1mkeA00', '2iybB00', '1xodA00',
           '2xqnM00', '1qc6B00', '1i2hA00', '1i7aA00', '2iybC00', '2iybA00', 
           '1i7aC00', '1ddwA00', '4my6B00', '1egxA00', '1tj6B00', '4my6A00',
           '2ifsA00', '1tj6A00', '2p8vA00', '1ddvA00', '3syxA00', '2jp2A00', 
           '2qkmC00', '5kq1A00', '4b6hB00', '2qkmA00', '5j3tA00', '2qkmE00',
           '1q67B01', '2qkmG00', '4b6hA00', '5kq1D00', '1q67A01', '2qklA00',
           '5lopB01', '5kq4D00', '5j3yC00', '5j3yA00', '5j3qC00', '5jp4A00',
           '5j3qA00', '5lonB01', '2lydA00', '5kq4A00']



allPH = []
PTBID = []
RanBDID = []
EVHID = []
DcpID = []
folder_path = "/Users/Kamilla/documents/data/all_PH_raw"
for filename in glob.glob(os.path.join(folder_path, '*.pdb')):
    with open (filename, "r") as f:
        allPH.append(filename[41:48])
 

for code in allPH:
    if code[0:4].upper() in Dcp:
        DcpID.append(code)         
        
print(DcpID)
print(len(DcpID))
        
for code in DcpID:
    print(code)

  



### Testing throughout writing               
# for code in allPH:
#     if code[0:4].upper() in EVH:
#         EVHID.append(code)         
        
# print(EVHID)
# print(len(EVHID))
        
# for code in EVHID:
#     print(code)



# folder_path = '/some/path/to/file'
# for filename in glob.glob(os.path.join(folder_path, '*.htm')):
#   with open(filename, 'r') as f:
#     text = f.read()
#     print (filename)
#     print (len(text))



# with open (sys.argv[1], "r") as cath:
#     cath_S = []
#     lines = cath.readlines()
#     for line in lines:
#         cath_S.append(line[0:7])


# def find_sequence(filename_pdb, filename_txt):
#     """Get the AA sequence from a PDB file and save it in a text file"""
#     with open(filename_pdb, "r") as pdb_file, open(filename_txt, "a") as seq_file:
#         ca_lines = []
#         sequence = ""
#         lines = pdb_file.readlines()


# for file in sys.argv[3:]:
#     if str(file[10:17]) in PTB:
#         find_sequence(file, sys.argv[2])





