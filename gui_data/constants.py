import platform

#Platform Details
OPERATING_SYSTEM = platform.system()
SYSTEM_ARCH = platform.platform()
SYSTEM_PROC = platform.processor()
ARM = 'arm'

is_macos = False

CPU = 'cpu'
CUDA_DEVICE = 'cuda'
DIRECTML_DEVICE = "privateuseone"

#MAIN_FONT_NAME = "Century Gothic"
OPT_SEPARATOR_SAVE = '─'*25
BG_COLOR = '#0e0e0f'
FG_COLOR = '#13849f'

#Model Types
VR_ARCH_TYPE = 'VR 架构'
MDX_ARCH_TYPE = 'MDX-Net'
DEMUCS_ARCH_TYPE = 'Demucs'
VR_ARCH_PM = 'VR 架构'
ENSEMBLE_MODE = '集成模式'
ENSEMBLE_STEM_CHECK = '集成音轨'
SECONDARY_MODEL = '辅助模型'
DEMUCS_6_STEM_MODEL = 'htdemucs_6s'
DEFAULT = "默认"
ALIGNMENT_TOOL = '对齐工具选项'

SINGLE_FILE = '单文件'
MULTIPLE_FILE = '多文件'
MAIN_MULTIPLE_FILE = '主多文件'
CHOOSE_EXPORT_FIR = '选择导出优先'

DUAL = "双轨"
FOUR_STEM = "四音轨"
ANY_STEM = "任意音轨"

DEMUCS_V3_ARCH_TYPE = 'Demucs v3'
DEMUCS_V4_ARCH_TYPE = 'Demucs v4'
DEMUCS_NEWER_ARCH_TYPES = [DEMUCS_V3_ARCH_TYPE, DEMUCS_V4_ARCH_TYPE]

DEMUCS_V1 = 'v1'
DEMUCS_V2 = 'v2'
DEMUCS_V3 = 'v3'
DEMUCS_V4 = 'v4'

DEMUCS_V1_TAG = 'v1 | '
DEMUCS_V2_TAG = 'v2 | '
DEMUCS_V3_TAG = 'v3 | '
DEMUCS_V4_TAG = 'v4 | '
DEMUCS_NEWER_TAGS = [DEMUCS_V3_TAG, DEMUCS_V4_TAG]

DEMUCS_VERSION_MAPPER = {
            DEMUCS_V1:DEMUCS_V1_TAG,
            DEMUCS_V2:DEMUCS_V2_TAG,
            DEMUCS_V3:DEMUCS_V3_TAG,
            DEMUCS_V4:DEMUCS_V4_TAG}

#Download Center
DOWNLOAD_FAILED = '下载失败'
DOWNLOAD_STOPPED = '下载已停止'
DOWNLOAD_COMPLETE = '下载完成'
DOWNLOAD_UPDATE_COMPLETE = '更新下载完成'
SETTINGS_MENU_EXIT = '退出'
NO_CONNECTION = '无网络连接'
VIP_SELECTION = 'VIP:'
DEVELOPER_SELECTION = 'VIP:'
NO_NEW_MODELS = '所有可用模型已下载'
ENSEMBLE_PARTITION = ': '
NO_MODEL = '未选择模型'
CHOOSE_MODEL = '选择模型'
SINGLE_DOWNLOAD = '正在下载项目 1/1...'
DOWNLOADING_ITEM = '正在下载项目'
FILE_EXISTS = '文件已存在！'
DOWNLOADING_UPDATE = '正在下载更新...'
DOWNLOAD_MORE = '下载更多模型'
IS_KARAOKEE = "is_karaoke"
IS_BV_MODEL = "is_bv_model"
IS_BV_MODEL_REBAL = "is_bv_model_rebalanced"
INPUT_STEM_NAME = '输入音轨名称'

#Menu Options

AUTO_SELECT = '自动'

#LINKS
DOWNLOAD_CHECKS = "https://raw.githubusercontent.com/TRvlvr/application_data/main/filelists/download_checks.json"
MDX_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_data_new.json"
VR_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/vr_model_data/model_data_new.json"
MDX23_CONFIG_CHECKS = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/mdx_c_configs/"
BULLETIN_CHECK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/bulletin.txt"

DEMUCS_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/demucs_model_data/model_name_mapper.json"
MDX_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_name_mapper.json"

DONATE_LINK_BMAC = "https://www.buymeacoffee.com/uvr5"
DONATE_LINK_PATREON = "https://www.patreon.com/uvr"

#DOWNLOAD REPOS
NORMAL_REPO = "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/"
UPDATE_REPO = "https://github.com/TRvlvr/model_repo/releases/download/uvr_update_patches/"

UPDATE_MAC_ARM_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_arm64.dmg"
UPDATE_MAC_X86_64_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_x86_64.dmg"
UPDATE_LINUX_REPO = "https://github.com/Anjok07/ultimatevocalremovergui#linux-installation"

ISSUE_LINK = 'https://github.com/Anjok07/ultimatevocalremovergui/issues/new'
VIP_REPO = b'\xf3\xc2W\x19\x1foI)\xc2\xa9\xcc\xb67(Z\xf5',\
           b'gAAAAABjQAIQ-NpNMMxMedpKHHb7ze_nqB05hw0YhbOy3pFzuzDrfqumn8_qvraxEoUpZC5ZXC0gGvfDxFMqyq9VWbYKlA67SUFI_wZB6QoVyGI581vs7kaGfUqlXHIdDS6tQ_U-BfjbEAK9EU_74-R2zXjz8Xzekw=='
NO_CODE = 'incorrect_code'

#Extensions
ONNX = '.onnx'
CKPT = '.ckpt'
CKPT_C = '.ckptc'
YAML = '.yaml'
PTH = '.pth'
TH_EXT = '.th'
JSON = '.json'

#GUI Buttons
START_PROCESSING = '开始处理'
WAIT_PROCESSING = '请稍候...'
STOP_PROCESSING = '正在停止处理，请稍候...'
LOADING_MODELS = '正在加载模型...'

#---Messages and Logs----

MISSING_MODEL = '缺失'
MODEL_PRESENT = '存在'

ALL_STEMS = '所有音轨'
VOCAL_STEM = '人声'
INST_STEM = '伴奏'
OTHER_STEM = '其他'
BASS_STEM = '贝斯'
DRUM_STEM = '鼓'
GUITAR_STEM = '吉他'
PIANO_STEM = '钢琴'
SYNTH_STEM = '合成器'
STRINGS_STEM = '弦乐'
WOODWINDS_STEM = '木管'
BRASS_STEM = '铜管'
WIND_INST_STEM = '管乐'
NO_OTHER_STEM = '无其他'
NO_BASS_STEM = '无贝斯'
NO_DRUM_STEM = '无鼓'
NO_GUITAR_STEM = '无吉他'
NO_PIANO_STEM = '无钢琴'
NO_SYNTH_STEM = '无合成器'
NO_STRINGS_STEM = '无弦乐'
NO_WOODWINDS_STEM = '无木管'
NO_WIND_INST_STEM = '无管乐'
NO_BRASS_STEM = '无铜管'
PRIMARY_STEM = '主音轨'
SECONDARY_STEM = '副音轨'
LEAD_VOCAL_STEM = 'lead_only'
BV_VOCAL_STEM = 'backing_only'
LEAD_VOCAL_STEM_I = 'with_lead_vocals'
BV_VOCAL_STEM_I = 'with_backing_vocals'
LEAD_VOCAL_STEM_LABEL = '主唱'
BV_VOCAL_STEM_LABEL = '伴唱'

VOCAL_STEM_ONLY = f'{VOCAL_STEM} 仅'
INST_STEM_ONLY = f'{INST_STEM} 仅'
PRIMARY_STEM_ONLY = f'{PRIMARY_STEM} 仅'

IS_SAVE_INST_ONLY = f'save_only_inst'
IS_SAVE_VOC_ONLY = f'save_only_voc'

DEVERB_MAPPER = {'仅主唱':VOCAL_STEM, 
                 '仅主唱':LEAD_VOCAL_STEM_LABEL, 
                 '仅伴唱':BV_VOCAL_STEM_LABEL, 
                 '所有人声类型':'ALL'}

BALANCE_VALUES = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

#Other Constants
DEMUCS_2_SOURCE = ["instrumental", "vocals"]
DEMUCS_4_SOURCE = ["drums", "bass", "other", "vocals"]

DEMUCS_2_SOURCE_MAPPER = {
                        INST_STEM: 0,
                        VOCAL_STEM: 1}

DEMUCS_4_SOURCE_MAPPER = {
                        BASS_STEM: 0,
                        DRUM_STEM: 1,
                        OTHER_STEM: 2,
                        VOCAL_STEM: 3}

DEMUCS_6_SOURCE_MAPPER = {
                        BASS_STEM:0,
                        DRUM_STEM:1,
                        OTHER_STEM:2,
                        VOCAL_STEM:3,
                        GUITAR_STEM:4,
                        PIANO_STEM:5}

DEMUCS_4_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM]
DEMUCS_6_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM, GUITAR_STEM, PIANO_STEM]

DEMUCS_UVR_MODEL = 'UVR_Model'

CHOOSE_STEM_PAIR = '选择音轨对'

STEM_SET_MENU = (VOCAL_STEM, 
                 INST_STEM, 
                 OTHER_STEM, 
                 BASS_STEM, 
                 DRUM_STEM, 
                 GUITAR_STEM, 
                 PIANO_STEM, 
                 SYNTH_STEM, 
                 STRINGS_STEM, 
                 WOODWINDS_STEM, 
                 BRASS_STEM, 
                 WIND_INST_STEM)

STEM_SET_MENU_ONLY = list(STEM_SET_MENU) + [OPT_SEPARATOR_SAVE, INPUT_STEM_NAME]

STEM_SET_MENU_2 = (
                 OTHER_STEM, 
                 BASS_STEM, 
                 DRUM_STEM, 
                 GUITAR_STEM, 
                 PIANO_STEM, 
                 SYNTH_STEM, 
                 STRINGS_STEM, 
                 WOODWINDS_STEM, 
                 BRASS_STEM, 
                 WIND_INST_STEM,
                 "噪声",
                 "混响")

STEM_PAIR_MAPPER = {
            VOCAL_STEM: INST_STEM,
            INST_STEM: VOCAL_STEM,
            LEAD_VOCAL_STEM: BV_VOCAL_STEM,
            BV_VOCAL_STEM: LEAD_VOCAL_STEM,
            PRIMARY_STEM: SECONDARY_STEM}

STEM_PAIR_MAPPER_FULL = {
            VOCAL_STEM: INST_STEM,
            INST_STEM: VOCAL_STEM,
            OTHER_STEM: NO_OTHER_STEM,
            BASS_STEM: NO_BASS_STEM,
            DRUM_STEM: NO_DRUM_STEM,
            GUITAR_STEM: NO_GUITAR_STEM,
            PIANO_STEM: NO_PIANO_STEM,
            SYNTH_STEM: NO_SYNTH_STEM,
            STRINGS_STEM: NO_STRINGS_STEM,
            WOODWINDS_STEM: NO_WOODWINDS_STEM,
            BRASS_STEM: NO_BRASS_STEM,
            WIND_INST_STEM: NO_WIND_INST_STEM,
            NO_OTHER_STEM: OTHER_STEM,
            NO_BASS_STEM: BASS_STEM,
            NO_DRUM_STEM: DRUM_STEM,
            NO_GUITAR_STEM: GUITAR_STEM,
            NO_PIANO_STEM: PIANO_STEM,
            NO_SYNTH_STEM: SYNTH_STEM,
            NO_STRINGS_STEM: STRINGS_STEM,
            NO_WOODWINDS_STEM: WOODWINDS_STEM,
            NO_BRASS_STEM: BRASS_STEM,
            NO_WIND_INST_STEM: WIND_INST_STEM,
            PRIMARY_STEM: SECONDARY_STEM}

NO_STEM = "无 "

NON_ACCOM_STEMS = (
            VOCAL_STEM,
            OTHER_STEM,
            BASS_STEM,
            DRUM_STEM,
            GUITAR_STEM,
            PIANO_STEM,
            SYNTH_STEM,
            STRINGS_STEM,
            WOODWINDS_STEM,
            BRASS_STEM,
            WIND_INST_STEM)

MDX_NET_FREQ_CUT = [VOCAL_STEM, INST_STEM]

DEMUCS_4_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM)
DEMUCS_6_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM, GUITAR_STEM, PIANO_STEM)
DEMUCS_2_STEM_OPTIONS = (VOCAL_STEM, INST_STEM)
DEMUCS_4_STEM_CHECK = (OTHER_STEM, BASS_STEM, DRUM_STEM)

#Menu Dropdowns

VOCAL_PAIR = f'{VOCAL_STEM}/{INST_STEM}'
INST_PAIR = f'{INST_STEM}/{VOCAL_STEM}'
OTHER_PAIR = f'{OTHER_STEM}/{NO_OTHER_STEM}'
DRUM_PAIR = f'{DRUM_STEM}/{NO_DRUM_STEM}'
BASS_PAIR = f'{BASS_STEM}/{NO_BASS_STEM}'
FOUR_STEM_ENSEMBLE = '四音轨集成'
MULTI_STEM_ENSEMBLE = '多音轨集成'

ENSEMBLE_MAIN_STEM = (CHOOSE_STEM_PAIR, VOCAL_PAIR, OTHER_PAIR, DRUM_PAIR, BASS_PAIR, FOUR_STEM_ENSEMBLE, MULTI_STEM_ENSEMBLE)

MIN_SPEC = '最小谱'
MAX_SPEC = '最大谱'
AUDIO_AVERAGE = '平均'

MAX_MIN = f'{MAX_SPEC}/{MIN_SPEC}'
MAX_MAX = f'{MAX_SPEC}/{MAX_SPEC}'
MAX_AVE = f'{MAX_SPEC}/{AUDIO_AVERAGE}'
MIN_MAX = f'{MIN_SPEC}/{MAX_SPEC}'
MIN_MIX = f'{MIN_SPEC}/{MIN_SPEC}'
MIN_AVE = f'{MIN_SPEC}/{AUDIO_AVERAGE}'
AVE_MAX = f'{AUDIO_AVERAGE}/{MAX_SPEC}'
AVE_MIN = f'{AUDIO_AVERAGE}/{MIN_SPEC}'
AVE_AVE = f'{AUDIO_AVERAGE}/{AUDIO_AVERAGE}'

ENSEMBLE_TYPE = (MAX_MIN, MAX_MAX, MAX_AVE, MIN_MAX, MIN_MIX, MIN_AVE, AVE_MAX, AVE_MIN, AVE_AVE)
ENSEMBLE_TYPE_4_STEM = (MAX_SPEC, MIN_SPEC, AUDIO_AVERAGE)

BATCH_MODE = '批量模式'
BETA_VERSION = '测试版'
DEF_OPT = '默认'
USER_INPUT = "用户输入"
OPT_SEPARATOR = '─'*65

CHUNKS = (AUTO_SELECT, '1', '5', '10', '15', '20', 
          '25', '30', '35', '40', '45', '50', 
          '55', '60', '65', '70', '75', '80', 
          '85', '90', '95', '完整')

BATCH_SIZE = (DEF_OPT, '2', '3', '4', '5', 
          '6', '7', '8', '9', '10')

VOL_COMPENSATION = (AUTO_SELECT, '1.035', '1.08')

MARGIN_SIZE = ('44100', '22050', '11025')

AUDIO_TOOLS = '音频工具'

MANUAL_ENSEMBLE = '手动集成'
TIME_STRETCH = '时间拉伸'
CHANGE_PITCH = '改变音高'
ALIGN_INPUTS = '对齐输入'
MATCH_INPUTS = '匹配处理'
COMBINE_INPUTS = '合并输入'

if OPERATING_SYSTEM == 'Windows' or OPERATING_SYSTEM == 'Darwin':  
   AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, TIME_STRETCH, CHANGE_PITCH, ALIGN_INPUTS, MATCH_INPUTS)
else:
   AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, ALIGN_INPUTS, MATCH_INPUTS)

MANUAL_ENSEMBLE_OPTIONS = (MIN_SPEC, MAX_SPEC, AUDIO_AVERAGE, COMBINE_INPUTS)

PROCESS_METHODS = (VR_ARCH_PM, MDX_ARCH_TYPE, DEMUCS_ARCH_TYPE, ENSEMBLE_MODE, AUDIO_TOOLS)

DEMUCS_SEGMENTS = (DEF_OPT, '1', '5', '10', '15', '20', 
                  '25', '30', '35', '40', '45', '50', 
                  '55', '60', '65', '70', '75', '80', 
                  '85', '90', '95', '100')

DEMUCS_SHIFTS = (0, 1, 2, 3, 4, 5, 
                 6, 7, 8, 9, 10, 11, 
                 12, 13, 14, 15, 16, 17, 
                 18, 19, 20)
SEMI_DEF = ['0']
SEMITONE_SEL = (-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12)

NOUT_SEL = (8, 16, 32, 48, 64)
NOUT_LSTM_SEL = (64, 128)

DEMUCS_OVERLAP = (0.25, 0.50, 0.75, 0.99)
MDX_OVERLAP = (DEF_OPT, 0.25, 0.50, 0.75, 0.99)
MDX23_OVERLAP = range(2, 51)
VR_AGGRESSION = range(0, 51)

TIME_WINDOW_MAPPER = {
            "无": None,
            "1": [0.0625],
            "2": [0.125],
            "3": [0.25],
            "4": [0.5],
            "5": [0.75],
            "6": [1],
            "7": [2],
            "偏移：低": [0.0625, 0.5],
            "偏移：中": [0.0625, 0.125, 0.5],
            "偏移：高": [0.0625, 0.125, 0.25, 0.5]
            #"偏移：非常高": [0.0625, 0.125, 0.25, 0.5, 0.75, 1],
}

INTRO_MAPPER = {
            "默认": [10],
            "1": [8],
            "2": [6],
            "3": [4],
            "4": [2],
            "偏移：低": [1, 10],
            "偏移：中": [1, 10, 8],
            "偏移：高": [1, 10, 8, 6, 4]
            }

VOLUME_MAPPER = {
            "无": (0, [0]),
            "低": (-4, range(0, 8)),
            "中": (-6, range(0, 12)),
            "高": (-6, [x * 0.5 for x in range(0, 25)]),
            "非常高": (-10, [x * 0.5 for x in range(0, 41)])}
            #"最大": (-10, [x * 0.3 for x in range(0, int(20 / 0.3) + 1)])}

PHASE_MAPPER = {
            "无": [0],
            "偏移低": [0, 180],
            "偏移中": [0],
            "偏移高": [0],
            "偏移非常高": [0],}

NONE_P = "无"
VLOW_P = "偏移：非常低"
LOW_P = "偏移：低"
MED_P = "偏移：中"
HIGH_P = "偏移：高"
VHIGH_P = "偏移：非常高"
VMAX_P = "偏移：最大"

PHASE_SHIFTS_OPT = {
                     NONE_P:190,
                     VLOW_P:180,
                     LOW_P:90,
                     MED_P:45,
                     HIGH_P:20,
                     VHIGH_P:10,
                     VMAX_P:1,}

VR_WINDOW = ('320', '512','1024')
VR_CROP = ('256', '512', '1024')
POST_PROCESSES_THREASHOLD_VALUES = ('0.1', '0.2', '0.3')

MDX_POP_PRO = ('MDX-NET_Noise_Profile_14_kHz', 'MDX-NET_Noise_Profile_17_kHz', 'MDX-NET_Noise_Profile_Full_Band')
MDX_POP_STEMS = ('人声', '伴奏', '其他', '鼓', '贝斯')
MDX_POP_NFFT = ('4096', '5120', '6144', '7680', '8192', '16384')
MDX_POP_DIMF = ('2048', '3072', '4096')
DENOISE_NONE, DENOISE_S, DENOISE_M = '无', '标准', '降噪模型'
MDX_DENOISE_OPTION = [DENOISE_NONE, DENOISE_S, DENOISE_M]
MDX_SEGMENTS = list(range(32, 4000+1, 32))

SAVE_ENSEMBLE = '保存集成'
CLEAR_ENSEMBLE = '清除选择'
MENU_SEPARATOR = 35*'•'
CHOOSE_ENSEMBLE_OPTION = '选择选项'
ALL_TYPES = '全部'
INVALID_ENTRY = '无效输入，请重试'
ENSEMBLE_INPUT_RULE = '1. 只允许字母、数字、空格和短横线。\n2. 开头或结尾不能有短横线或空格。'
STEM_INPUT_RULE = '1. 只允许无空格的单词。\n2. 不允许空格、数字或特殊字符。'

ENSEMBLE_OPTIONS = [OPT_SEPARATOR_SAVE, SAVE_ENSEMBLE, CLEAR_ENSEMBLE]
ENSEMBLE_CHECK = 'ensemble check'
KARAOKEE_CHECK = 'kara check'

AUTO_PHASE = "自动"
POSITIVE_PHASE = "正相位"
NEGATIVE_PHASE = "负相位"
OFF_PHASE = "原生相位"

ALIGN_PHASE_OPTIONS = [AUTO_PHASE, POSITIVE_PHASE, NEGATIVE_PHASE, OFF_PHASE]

SELECT_SAVED_ENSEMBLE = '选择已保存的集成'
SELECT_SAVED_SETTING = '选择已保存的设置'
ENSEMBLE_OPTION = "集成自定义选项"
MDX_OPTION = "高级 MDX-Net 选项"
DEMUCS_OPTION = "高级 Demucs 选项"
VR_OPTION = "高级 VR 选项"
HELP_OPTION = "打开信息指南"
ERROR_OPTION = "打开错误日志"
VERIFY_BEGIN = '正在验证文件 '
SAMPLE_BEGIN = '正在创建样本 '
MODEL_MISSING_CHECK = '模型缺失:'
OPTION_LIST = [VR_OPTION, MDX_OPTION, DEMUCS_OPTION, ENSEMBLE_OPTION, ALIGNMENT_TOOL, HELP_OPTION, ERROR_OPTION]

#Menu Strings
VR_MENU ='VR 菜单'
DEMUCS_MENU ='Demucs 菜单'
MDX_MENU ='MDX-Net 菜单'
ENSEMBLE_MENU ='集成菜单'
HELP_MENU ='帮助菜单'
ERROR_MENU ='错误日志'
INPUTS_MENU ='输入菜单'
ALIGN_MENU ='对齐菜单'

# Audio Player
PLAYING_SONG = ": 播放中"
PAUSE_SONG = ": 已暂停"
STOP_SONG = ": 已停止"

SELECTED_VER = '已选'
DETECTED_VER = '检测到'

SAMPLE_MODE_CHECKBOX = lambda v:f'样本模式 ({v}秒)'
REMOVED_FILES = lambda r, e:f'音频输入验证报告：\n\n已移除文件：\n\n{r}\n\n错误详情：\n\n{e}'
ADVANCED_SETTINGS = (ENSEMBLE_OPTION, MDX_OPTION, DEMUCS_OPTION, VR_OPTION, HELP_OPTION, ERROR_OPTION)

WAV = 'WAV'
FLAC = 'FLAC'
MP3 = 'MP3'

MP3_BIT_RATES = ('96k', '128k', '160k', '224k', '256k', '320k')
WAV_TYPE = ('PCM_U8', 'PCM_16', 'PCM_24', 'PCM_32', '32位浮点', '64位浮点')
GPU_DEVICE_NUM_OPTS = (DEFAULT, '0', '1', '2', '3', '4', '5', '6', '7', '8')

SELECT_SAVED_SET = '选择选项'
SAVE_SETTINGS = '保存当前设置'
RESET_TO_DEFAULT = '重置为默认'
RESET_FULL_TO_DEFAULT = '重置为默认'
RESET_PM_TO_DEFAULT = '重置所有应用设置为默认'

SAVE_SET_OPTIONS = [OPT_SEPARATOR_SAVE, SAVE_SETTINGS, RESET_TO_DEFAULT]

TIME_PITCH = ('1.0', '2.0', '3.0', '4.0')
TIME_TEXT = '_time_stretched'
PITCH_TEXT = '_pitch_shifted'

#RegEx Input Validation
REG_PITCH = r'^[-+]?(1[0]|[0-9]([.][0-9]*)?)$'
REG_TIME = r'^[+]?(1[0]|[0-9]([.][0-9]*)?)$'
REG_COMPENSATION = r'\b^(1[0]|[0-9]([.][0-9]*)?|Auto|None)$\b'
REG_THES_POSTPORCESS = r'\b^([0]([.][0-9]{0,6})?)$\b'
REG_CHUNKS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Auto|Full)$\b'
REG_CHUNKS_DEMUCS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Auto|Full)$\b'
REG_MARGIN = r'\b^[0-9]*$\b'
REG_SEGMENTS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Default)$\b'
REG_SAVE_INPUT = r'\b^([a-zA-Z0-9 -]{0,25})$\b'
REG_INPUT_STEM_NAME = r'^(Wind Inst|[a-zA-Z]{1,25})$'
REG_SEMITONES = r'^-?(20\.00|[01]?\d(\.\d{1,2})?|20)$'
REG_AGGRESSION = r'^[-+]?[0-9]\d*?$'
REG_WINDOW = r'\b^[0-9]{0,4}$\b'
REG_SHIFTS = r'\b^[0-9]*$\b'
REG_BATCHES = r'\b^([0-9]*?|Default)$\b'
REG_OVERLAP = r'\b^([0]([.][0-9]{0,6})?|Default)$\b'#r"(Default|[0-9]+(\.[0-9]+)?)"#
REG_OVERLAP23 = r'\b^([1][0-9]|[2-9][0-9]*|Default)$\b'#r'\b^([2-9][0-9]*?|Default)$\b'
REG_MDX_SEG = r'\b(?:' + '|'.join([str(num) for num in range(32, 1000001, 32)]) + r')\b'
REG_ALIGN = r'^[-+]?[0-9]\d*?$'
REG_VOL_COMP = r'^\d+\.\d{1,9}$'

# Sub Menu
VR_ARCH_SETTING_LOAD = '为 VR 架构加载'
MDX_SETTING_LOAD = '为 MDX-Net 加载'
DEMUCS_SETTING_LOAD = '为 Demucs 加载'
ALL_ARCH_SETTING_LOAD = '为整个应用加载'

# Mappers

DEFAULT_DATA = {
        'chosen_process_method': MDX_ARCH_TYPE,
        'vr_model': CHOOSE_MODEL,
        'aggression_setting': 5,
        'window_size': 512,
        'mdx_segment_size': 256,
        'batch_size': DEF_OPT,
        'crop_size': 256, 
        'is_tta': False,
        'is_output_image': False,
        'is_post_process': False,
        'is_high_end_process': False,
        'post_process_threshold': 0.2,
        'vr_voc_inst_secondary_model': NO_MODEL,
        'vr_other_secondary_model': NO_MODEL,
        'vr_bass_secondary_model': NO_MODEL,
        'vr_drums_secondary_model': NO_MODEL,
        'vr_is_secondary_model_activate': False,        
        'vr_voc_inst_secondary_model_scale': 0.9,
        'vr_other_secondary_model_scale': 0.7,
        'vr_bass_secondary_model_scale': 0.5,
        'vr_drums_secondary_model_scale': 0.5,
        'demucs_model': CHOOSE_MODEL, 
        'segment': DEMUCS_SEGMENTS[0],
        'overlap': DEMUCS_OVERLAP[0],
        'overlap_mdx': MDX_OVERLAP[0],
        'overlap_mdx23': '8',
        'shifts': 2,
        'chunks_demucs': CHUNKS[0],
        'margin_demucs': 44100,
        'is_chunk_demucs': False,
        'is_chunk_mdxnet': False,
        'is_primary_stem_only_Demucs': False,
        'is_secondary_stem_only_Demucs': False,
        'is_split_mode': True,
        'is_demucs_combine_stems': True,#
        'is_mdx23_combine_stems': True,#
        'demucs_voc_inst_secondary_model': NO_MODEL,
        'demucs_other_secondary_model': NO_MODEL,
        'demucs_bass_secondary_model': NO_MODEL,
        'demucs_drums_secondary_model': NO_MODEL,
        'demucs_is_secondary_model_activate': False,        
        'demucs_voc_inst_secondary_model_scale': 0.9,
        'demucs_other_secondary_model_scale': 0.7,
        'demucs_bass_secondary_model_scale': 0.5,
        'demucs_drums_secondary_model_scale': 0.5,
        'demucs_stems': ALL_STEMS,
        'demucs_pre_proc_model': NO_MODEL,
        'is_demucs_pre_proc_model_activate': False,
        'is_demucs_pre_proc_model_inst_mix': False,
        'mdx_net_model': CHOOSE_MODEL,
        'chunks': CHUNKS[0],
        'margin': 44100,
        'compensate': AUTO_SELECT,
        'is_denoise': False,#
        'denoise_option': 'None',#
        'phase_option': AUTO_PHASE,
        'phase_shifts': NONE_P,#
        'is_save_align': False,#, 
        'is_match_frequency_pitch': True,#
        'is_match_silence': True,#
        'is_spec_match': False,#
        'is_mdx_c_seg_def': False,
        'is_invert_spec': False, #
        'is_deverb_vocals': False, #
        'deverb_vocal_opt': 'Main Vocals Only', #
        'voc_split_save_opt': 'Lead Only', #
        'is_mixer_mode': False, 
        'mdx_batch_size': DEF_OPT,
        'mdx_voc_inst_secondary_model': NO_MODEL,
        'mdx_other_secondary_model': NO_MODEL,
        'mdx_bass_secondary_model': NO_MODEL,
        'mdx_drums_secondary_model': NO_MODEL,
        'mdx_is_secondary_model_activate': False,        
        'mdx_voc_inst_secondary_model_scale': 0.9,
        'mdx_other_secondary_model_scale': 0.7,
        'mdx_bass_secondary_model_scale': 0.5,
        'mdx_drums_secondary_model_scale': 0.5,
        'mdx_stems': ALL_STEMS,
        'is_save_all_outputs_ensemble': True,
        'is_append_ensemble_name': False,
        'chosen_audio_tool': AUDIO_TOOL_OPTIONS[0],
        'choose_algorithm': MANUAL_ENSEMBLE_OPTIONS[0],
        'time_stretch_rate': 2.0,
        'pitch_rate': 2.0,
        'is_time_correction': True,
        'is_gpu_conversion': False,
        'is_primary_stem_only': False,
        'is_secondary_stem_only': False,
        'is_testing_audio': False,#
        'is_auto_update_model_params': True,#
        'is_add_model_name': False,
        'is_accept_any_input': False,
        'is_task_complete': False,
        'is_normalization': False,
        'is_use_opencl': False,
        'is_wav_ensemble': False,
        'is_create_model_folder': False,
        'mp3_bit_set': '320k',#
        'semitone_shift': '0',#
        'save_format': WAV,
        'wav_type_set': 'PCM_16',
        'device_set': DEFAULT,
        'user_code': '',
        'export_path': '',
        'input_paths': [],
        'lastDir': None,
        'time_window': "3",
        'intro_analysis': DEFAULT,
        'db_analysis': "Medium",
        'fileOneEntry': '',
        'fileOneEntry_Full': '',
        'fileTwoEntry': '',
        'fileTwoEntry_Full': '',
        'DualBatch_inputPaths': [],
        'model_hash_table': {},
        'help_hints_var': True,
        'set_vocal_splitter': NO_MODEL,
        'is_set_vocal_splitter': False,#
        'is_save_inst_set_vocal_splitter': False,#
        'model_sample_mode': False,
        'model_sample_mode_duration': 30
}

SETTING_CHECK = ('vr_model',
               'aggression_setting',
               'window_size',
               'mdx_segment_size',
               'batch_size',
               'crop_size',
               'is_tta',
               'is_output_image',
               'is_post_process',
               'is_high_end_process',
               'post_process_threshold',
               'vr_voc_inst_secondary_model',
               'vr_other_secondary_model',
               'vr_bass_secondary_model',
               'vr_drums_secondary_model',
               'vr_is_secondary_model_activate',
               'vr_voc_inst_secondary_model_scale',
               'vr_other_secondary_model_scale',
               'vr_bass_secondary_model_scale',
               'vr_drums_secondary_model_scale',
               'demucs_model',
               'segment',
               'overlap',
               'overlap_mdx',
               'shifts',
               'chunks_demucs',
               'margin_demucs',
               'is_chunk_demucs',
               'is_primary_stem_only_Demucs',
               'is_secondary_stem_only_Demucs',
               'is_split_mode',
               'is_demucs_combine_stems',#
               'is_mdx23_combine_stems',#
               'demucs_voc_inst_secondary_model',
               'demucs_other_secondary_model',
               'demucs_bass_secondary_model',
               'demucs_drums_secondary_model',
               'demucs_is_secondary_model_activate',
               'demucs_voc_inst_secondary_model_scale',
               'demucs_other_secondary_model_scale',
               'demucs_bass_secondary_model_scale',
               'demucs_drums_secondary_model_scale',
               'demucs_stems',
               'mdx_net_model',
               'chunks',
               'margin',
               'compensate',
               'is_denoise',#
               'denoise_option',#
               'phase_option',#
               'phase_shifts',#
               'is_save_align',#,
               'is_match_silence',
               'is_spec_match',#,
               'is_match_frequency_pitch',#
               'is_mdx_c_seg_def',
               'is_invert_spec',#
               'is_deverb_vocals',#
               'deverb_vocal_opt',#
               'voc_split_save_opt',#
               'mdx_batch_size',
               'mdx_voc_inst_secondary_model',
               'mdx_other_secondary_model',
               'mdx_bass_secondary_model',
               'mdx_drums_secondary_model',
               'mdx_is_secondary_model_activate',
               'mdx_voc_inst_secondary_model_scale',
               'mdx_other_secondary_model_scale',
               'mdx_bass_secondary_model_scale',
               'mdx_drums_secondary_model_scale',
               'is_save_all_outputs_ensemble',
               'is_append_ensemble_name',
               'chosen_audio_tool',
               'choose_algorithm',
               'time_stretch_rate',
               'pitch_rate',
               'is_time_correction',
               'is_primary_stem_only',
               'is_secondary_stem_only',
               'is_testing_audio',#
               'is_auto_update_model_params',#
               'is_add_model_name',
               "is_accept_any_input",
               'is_task_complete',
               'is_create_model_folder',
               'mp3_bit_set',#
               'semitone_shift',#
               'save_format',
               'wav_type_set',
               'device_set',
               'user_code',
               'is_gpu_conversion',
               'is_normalization',
               'is_use_opencl',
               'is_wav_ensemble',
               'help_hints_var',
               'set_vocal_splitter',
               'is_set_vocal_splitter',#
               'is_save_inst_set_vocal_splitter',#
               'model_sample_mode',
               'model_sample_mode_duration',
               'time_window',
               'intro_analysis',
               'db_analysis',
               'fileOneEntry',
               'fileOneEntry_Full',
               'fileTwoEntry',
               'fileTwoEntry_Full',
               'DualBatch_inputPaths'
               )

NEW_LINES = "\n\n"
NEW_LINE = "\n"
NO_LINE = ''

FFMPEG_EXT = (".aac", ".aiff", ".alac" ,".flac", ".FLAC", ".mov", ".mp4", ".MP4", 
              ".m4a", ".M4A", ".mp2", ".mp3", "MP3", ".mpc", ".mpc8", 
              ".mpeg", ".ogg", ".OGG", ".tta", ".wav", ".wave", ".WAV", ".WAVE", ".wma", ".webm", ".eac3", ".mkv", ".opus", ".OPUS")

FFMPEG_MORE_EXT = (".aa", ".aac", ".ac3", ".aiff", ".alac", ".avi", ".f4v",".flac", ".flic", ".flv",
              ".m4v",".mlv", ".mov", ".mp4", ".m4a", ".mp2", ".mp3", ".mp4", ".mpc", ".mpc8", 
              ".mpeg", ".ogg", ".tta", ".tty", ".vcd", ".wav", ".wma")
ANY_EXT = ""

# Secondary Menu Constants

VOCAL_PAIR_PLACEMENT = 1, 2, 3, 4
OTHER_PAIR_PLACEMENT = 5, 6, 7, 8
BASS_PAIR_PLACEMENT = 9, 10, 11, 12
DRUMS_PAIR_PLACEMENT = 13, 14, 15, 16

# Drag n Drop String Checks

DOUBLE_BRACKET = "} {"
RIGHT_BRACKET = "}"
LEFT_BRACKET = "{"
#DND CONSTS

MAC_DND_CHECK = ('/Users/',
                 '/Applications/',
                 '/Library/',
                 '/System/')
LINUX_DND_CHECK = ('/home/',
                   '/usr/')
WINDOWS_DND_CHECK = ('A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:')

WOOD_INST_MODEL_HASH = '0ec76fd9e65f81d8b4fbd13af4826ed8'
WOOD_INST_PARAMS = {
    "vr_model_param": "4band_v3",
    "primary_stem": NO_WIND_INST_STEM
                     }

READ_ONLY = 'readonly'

FILE_1 = 'file1'
FILE_2 = 'file2'

FILE_1_LB = 'file1_lb'
FILE_2_LB = 'file1_2b'
BATCH_MODE_DUAL = " : 批量模式"

CODEC_DICT = {
    'PCM_U8':   {"sample_width": 1, "codec": None},        # 8-bit unsigned PCM
    'PCM_16':   {"sample_width": 2, "codec": None},        # 16-bit signed PCM
    'PCM_24':   {"sample_width": 3, "codec": None},        # 24-bit signed PCM
    'PCM_32':   {"sample_width": 4, "codec": None},        # 32-bit signed PCM
    'FLOAT32':  {"sample_width": None, "codec": "pcm_f32le"},  # 32-bit float
    'FLOAT64':  {"sample_width": None, "codec": "pcm_f64le"}   # 64-bit float
}


# Manual Downloads
VR_PLACEMENT_TEXT = '将模型放置在 \"models/VR_Models\" 目录中。'
MDX_PLACEMENT_TEXT = '将模型放置在 \"models/MDX_Net_Models\" 目录中。'
DEMUCS_PLACEMENT_TEXT = '将模型放置在 \"models/Demucs_Models\" 目录中。'
DEMUCS_V3_V4_PLACEMENT_TEXT = '将项目放置在 \"models/Demucs_Models/v3_v4_repo\" 目录中。'
MDX_23_NAME = "MDX23C 模型"

# Liscense info
if OPERATING_SYSTEM=="Darwin":
   is_macos = True
   LICENSE_OS_SPECIFIC_TEXT = '• 本应用适用于运行 macOS Catalina 及以上版本的系统。\n' +\
                              '• 不保证在 macOS Mojave 或更低版本系统上的功能。\n' +\
                              '• 不保证在老旧或低配置 Mac 系统上的功能。\n\n'
elif OPERATING_SYSTEM=="Linux":
   LICENSE_OS_SPECIFIC_TEXT = '• 本应用适用于运行 Linux Ubuntu 18.04+ 的系统。\n' +\
                              '• 不保证在其他 Linux 平台上的功能。\n' +\
                              '• 不保证在老旧或低配置系统上的功能。\n\n'
elif OPERATING_SYSTEM=="Windows":
   LICENSE_OS_SPECIFIC_TEXT = '• 本应用适用于运行 Windows 10 或更高版本的系统。\n' +\
                              '• 不保证在 Windows 7 或更低版本系统上的功能。\n' +\
                              '• 不保证在 Intel Pentium 和 Celeron CPU 系统上的功能。\n\n'

LICENSE_TEXT = lambda a, p:f'当前应用版本：Ultimate Vocal Remover {a}\n' +\
               f'当前补丁版本：{p}\n\n' +\
               '版权所有 (c) 2022 Ultimate Vocal Remover\n\n' +\
               'UVR 是免费开源软件，采用 MIT 许可证。如果您在与 UVR 无关的项目中使用我们的\n' +\
               f'模型或代码，请注明出处。\n\n{LICENSE_OS_SPECIFIC_TEXT}' +\
               '本捆绑包包含 UVR 界面、Python、PyTorch 以及其他\n' +\
               '有效运行应用所需的依赖项。\n\n' +\
               '网站链接：本应用、系统或服务可能包含指向其他网站和下载内容的链接，\n' +\
               '这些链接仅作为附加便利提供给您。您理解并确认，点击或激活此类链接\n' +\
               '即表示您正在访问本应用之外的站点或服务，我们不会筛选、审查、批准\n' +\
               '或以其他方式认可这些链接网站中包含的任何内容或信息。\n' +\
               '您承认并同意，我们、我们的关联公司和合作伙伴不对这些链接网站的内容\n' +\
               '负责，包括链接网站提供的信息的准确性或可用性，并且我们不对您使用\n' +\
               '链接网站作任何陈述或保证。\n\n' +\
               '本应用采用 MIT 许可证\n\n' +\
               '特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人\n' +\
               '不受限制地处理本软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售\n' +\
               '本软件副本的权利，并允许获得本软件的人这样做，但须遵守以下条件：\n\n' +\
               '上述版权声明和本许可声明应包含在本软件的所有\n' +\
               '副本或重要部分中。\n\n' +\
               '本软件按“原样”提供，不提供任何形式的明示或暗示的保证，包括但不限于\n' +\
               '适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或\n' +\
               '版权持有人均不对因本软件或使用或与本软件有关的其他交易\n' +\
               '引起的任何索赔、损害或其他责任负责，无论是合同诉讼、侵权诉讼还是其他诉讼。'

# Message Box Text
INVALID_INPUT = '无效输入', '输入无效。\n\n请确认输入仍然存在或有效，然后重试。'
INVALID_EXPORT = '无效的导出目录', '您选择了无效的导出目录。\n\n请确保所选目录仍然存在。'
INVALID_ENSEMBLE = '模型不足', '您必须选择 2 个或更多模型才能运行集成。'
INVALID_MODEL = '未选择模型', '您必须选择一个模型才能继续。'
MISSING_MODEL = '模型缺失', '所选模型缺失或无效。'
ERROR_OCCURED = '发生错误', '\n\n是否要打开错误日志以查看详细信息？\n'
PROCESS_COMPLETE = '\n处理完成\n'
PROCESS_COMPLETE_2 = '处理完成\n'

# GUI Text Constants
BACK_TO_MAIN_MENU = '返回主菜单'

# Help Hint Text
INTERNAL_MODEL_ATT = '这是一个内部模型设置。\n\n***除非您非常确定，否则请勿更改！***'
STOP_HELP = '停止正在进行的任务。\n• 停止前会出现确认弹窗。'
SETTINGS_HELP = '访问主设置和“下载中心”。'
COMMAND_TEXT_HELP = '显示正在进行的任务的状态和进度。'
SAVE_CURRENT_SETTINGS_HELP = '加载或保存应用的设置。'
PITCH_SHIFT_HELP = ('为处理音轨选择音高：\n\n'
                '• 整数表示半音。\n'
                '• 使用较高的音高可能会削减高端带宽，即使在高质量模型中也是如此。\n'
                '• 提高音高对于人声较深的音轨可能更好。\n'
                '• 降低音高可能需要更多处理时间，但适用于人声音调较高的音轨。')
AGGRESSION_SETTING_HELP = ('调整主音轨提取的强度：\n\n'
                           '• 范围从 -100 到 100。\n'
                           '• 值越大，提取越深入。\n' 
                           '• 通常，人声和伴奏设置为 5。\n' 
                           '• 对于非人声模型，超过 5 的值可能会使声音变得浑浊。')
WINDOW_SIZE_HELP = ('选择窗口大小以平衡质量和速度：\n\n'
                    '• 1024 - 快速但质量较低。\n'
                    '• 512 - 速度和质量中等。\n'
                    '• 320 - 耗时更长，但可能提供更好的质量。')
MDX_SEGMENT_SIZE_HELP = ('选择段大小以平衡速度、资源使用和质量：\n'
                         '• 较小的段消耗较少资源。\n'
                         '• 较大的段消耗更多资源，但可能提供更好的结果。\n'
                         '• 默认大小为 256。质量会因您的选择而异。')
DEMUCS_STEMS_HELP = ('使用所选模型选择要提取的音轨：\n\n'
                     '• 所有音轨 - 提取所有可用音轨。\n'
                     '• 人声 - 仅“人声”音轨。\n'
                     '• 其他 - 仅“其他”音轨。\n'
                     '• 贝斯 - 仅“贝斯”音轨。\n'
                     '• 鼓 - 仅“鼓”音轨。')
SEGMENT_HELP = ('调整段以管理 RAM 或显存使用：\n\n'
               '• 较小的段消耗较少资源。\n'
               '• 较大的段消耗更多资源，但可能提供更好的结果。\n'
               '• “默认”选择最佳大小。')

ENSEMBLE_MAIN_STEM_HELP = (
    '选择用于集成的音轨类型：\n\n'
    
    f'• {VOCAL_PAIR}：\n'
    '  - 主音轨：人声\n'
    '  - 副音轨：伴奏（混合音减去人声）\n\n'
    
    f'• {OTHER_PAIR}：\n'
    '  - 主音轨：其他\n'
    '  - 副音轨：无其他（混合音减去“其他”）\n\n'
    
    f'• {BASS_PAIR}：\n'
    '  - 主音轨：贝斯\n'
    '  - 副音轨：无贝斯（混合音减去贝斯）\n\n'
    
    f'• {DRUM_PAIR}：\n'
    '  - 主音轨：鼓\n'
    '  - 副音轨：无鼓（混合音减去鼓）\n\n'
    
    f'• {FOUR_STEM_ENSEMBLE}：\n'
    '  - 收集所有 4 音轨 Demucs 模型并集成所有输出。\n\n'
    
    f'• {MULTI_STEM_ENSEMBLE}：\n'
    '  - “丛林集成”收集所有模型并集成任何相关输出。'
)

ENSEMBLE_TYPE_HELP = (
    '选择用于生成最终输出的集成算法：\n\n'
    
    f'• {MAX_MIN}：\n'
    '  - 主音轨使用“最大谱”算法处理。\n'
    '  - 副音轨使用“最小谱”算法处理。\n\n'
    
    '注意：对于“四音轨集成”选项，只会显示一个算法。\n\n'
    
    '算法详情：\n'
    
    f'• {MAX_SPEC}：\n'
    '  - 产生尽可能高的输出。\n'
    '  - 适用于人声音轨以获得更饱满的声音，但可能引入不必要的伪影。\n'
    '  - 适用于伴奏音轨，但避免在集成中使用 VR 架构模型。\n\n'
    
    f'• {MIN_SPEC}：\n'
    '  - 产生尽可能低的输出。\n'
    '  - 适用于伴奏音轨以获得更干净的结果。可能导致“浑浊”的声音。\n\n'
    
    f'• {AUDIO_AVERAGE}：\n'
    '  - 将所有结果平均以得到最终输出。'
)

ENSEMBLE_LISTBOX_HELP = (
    '显示所选主音轨对的所有可用模型。'
)

if OPERATING_SYSTEM == 'darwin':
   IS_GPU_CONVERSION_HELP = (
      '• 使用 GPU 进行处理（如果可用）：\n'
      '  - 如果选中，应用将尝试使用您的 GPU 以加快处理速度。\n'
      '  - 如果未检测到 GPU，将默认使用 CPU 处理。\n'
      '  - macOS 的 GPU 处理仅适用于 VR 架构模型。\n\n'
      '• 请注意：\n'
      '  - CPU 处理明显慢于 GPU 处理。\n'
      '  - 只有配备 M1 芯片的 Mac 才能用于 GPU 处理。'
   )
else:
   IS_GPU_CONVERSION_HELP = (
      '• 使用 GPU 进行处理（如果可用）：\n'
      '  - 如果选中，应用将尝试使用您的 GPU 以加快处理速度。\n'
      '  - 如果未检测到 GPU，将默认使用 CPU 处理。\n\n'
      '• 请注意：\n'
      '  - CPU 处理明显慢于 GPU 处理。\n'
      '  - 只有 Nvidia GPU 可用于 GPU 处理。'
   )

IS_TIME_CORRECTION_HELP = ('选中后，输出将保留输入的原始 BPM。')
SAVE_STEM_ONLY_HELP = '允许用户仅保存所选音轨。'
IS_NORMALIZATION_HELP = '归一化输出以防止削波。'
IS_CUDA_SELECT_HELP = "如果您有多个 GPU，可以选择用于处理的 GPU。"
CROP_SIZE_HELP = '**仅与部分模型兼容！**\n\n 设置应与训练裁剪大小值匹配。如果不确定，请保持原样。'
IS_TTA_HELP = ('此选项执行测试时增强以提高分离质量。\n\n'
               '注意：选中此选项将增加完成转换所需的时间。')
IS_POST_PROCESS_HELP = ('此选项可以潜在地识别人声输出中残留的伴奏伪影。\n此选项可能会改善某些歌曲的分离效果。\n\n' +\
                       '注意：根据音轨的不同，选择此选项可能会对转换过程产生负面影响。因此，仅建议作为最后手段使用。')
IS_HIGH_END_PROCESS_HELP = '应用将镜像输出中缺失的频率范围。'
SHIFTS_HELP = ('对输入执行多次随机偏移预测并取平均值。\n\n'
              '• 偏移次数越多，预测时间越长。\n- 除非您有 GPU，否则不建议使用。')
OVERLAP_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
               '       - 较高的值可以提供更好的结果，但会导致更长的处理时间。\n'
               '       - 您可以选择 0.001-0.999 之间的值。')
MDX_OVERLAP_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
               '       - 较高的值可以提供更好的结果，但会导致更长的处理时间。\n'
               '       - 对于非 MDX23C 模型：您可以选择 0.001-0.999 之间的值。')
OVERLAP_23_HELP = ('• 此选项控制预测窗口之间的重叠量。\n'
                  '       - 较高的值可以提供更好的结果，但会导致更长的处理时间。')
IS_SEGMENT_DEFAULT_HELP = '• 段大小基于所选模型关联的配置（yaml）文件中提供的值设置。'
IS_SPLIT_MODE_HELP = '• 启用“段”。\n• 仅建议拥有强大电脑的用户取消选择此选项。'
IS_DEMUCS_COMBINE_STEMS_HELP = '应用将通过组合剩余音轨来创建副音轨，而不是将主音轨与混合音进行反相。'
COMPENSATE_HELP = '补偿主音轨的音频以获得更好的副音轨。'
IS_DENOISE_HELP = ('• 标准：此设置减少 MDX-Net 模型产生的噪音。\n' 
                   '       - 此选项仅减少非 MDX23 模型中的噪音。\n' 
                   '• 降噪模型：此设置使用特殊的降噪模型来消除任何 MDX-Net 模型产生的噪音。\n'
                   '       - 此选项适用于所有 MDX-Net 模型。\n'
                   '       - 您必须安装“UVR-DeNoise-Lite” VR 架构模型才能使用此选项。\n'
                   '• 请注意：这两个选项都会增加分离时间。')

VOC_SPLIT_MODEL_SELECT_HELP = '• 从主唱和伴唱模型列表中选择一个模型，以自动处理人声音轨。'
IS_VOC_SPLIT_INST_SAVE_SELECT_HELP = '• 激活后，您将获得额外的伴奏输出，包括：仅主唱和仅伴唱的输出。'
IS_VOC_SPLIT_MODEL_SELECT_HELP = ('• 激活后，此选项会自动处理生成的人声音轨，使用卡拉 OK 模型移除主唱或使用另一个模型移除伴唱。\n'
                                 '       - 此选项将人声音轨分成两个独立部分：主唱和伴唱，提供两个额外的人声输出。\n'
                                 '       - 无论您使用卡拉 OK 模型还是伴唱模型，结果的组织方式相同。\n'
                                 '       - 此选项目前不适用于集成模式。')
IS_DEVERB_OPT_HELP = ('• 选择您希望自动去除混响的人声类型。\n'
                     '       - 示例：选择“仅主唱”将仅从主唱音轨中去除混响。')
IS_DEVERB_VOC_HELP = ('• 此选项从人声音轨中去除混响。\n'
                     '       - 您必须安装“UVR-DeEcho-DeReverb” VR 架构模型才能使用此选项。\n'
                     '       - 此选项目前不适用于集成模式。')
IS_FREQUENCY_MATCH_HELP = '将主音轨的频率截止与副音轨的频率截止匹配。'
CLEAR_CACHE_HELP = '清除用户选择的未识别模型的设置。'
IS_SAVE_ALL_OUTPUTS_ENSEMBLE_HELP = '如果启用，将保留所有单独集成生成的输出。'
IS_APPEND_ENSEMBLE_NAME_HELP = '启用后，集成名称将添加到最终输出中。'
IS_WAV_ENSEMBLE_HELP = (
    '激活后，使用波形而不是频谱处理集成算法：\n'
    '• 可能导致失真增加。\n'
    '• 波形集成比频谱集成更快。'
)
DONATE_HELP = '打开官方 UVR “Buy Me a Coffee” 外部链接以支持项目！'
IS_INVERT_SPEC_HELP = (
    '潜在地提高副音轨质量：\n'
    '• 使用频谱而不是波形来反相主音轨。\n'
    '• 稍慢的反相方法。'
)
IS_TESTING_AUDIO_HELP = '在保存的文件后附加一个 10 位数字以避免意外覆盖。'
IS_MODEL_TESTING_AUDIO_HELP = '将模型名称附加到输出中，以便在不同模型之间进行比较。'
IS_ACCEPT_ANY_INPUT_HELP = (
    '启用后允许所有类型的输入，即使是非音频格式。\n'
    '仅用于实验目的。不建议常规使用。'
)
IS_TASK_COMPLETE_HELP = '激活后，在过程完成或失败时播放提示音。'
DELETE_YOUR_SETTINGS_HELP = (
    '包含您保存的设置。删除所选设置前会请求确认。'
)
SET_STEM_NAME_HELP = '为给定模型选择主音轨。'
IS_CREATE_MODEL_FOLDER_HELP = ('每次转换后，将在导出目录中为输出生成两个新目录。\n\n'
                              '• 示例：\n'
                              '─ 导出目录\n'
                              '   └── 第一个目录（以模型命名）\n'
                              '           └── 第二个目录（以音轨命名）\n'
                              '                    └── 输出文件')
MDX_DIM_T_SET_HELP = INTERNAL_MODEL_ATT
MDX_DIM_F_SET_HELP = INTERNAL_MODEL_ATT

MDX_N_FFT_SCALE_SET_HELP = '指定模型训练期间使用的 N_FFT 大小。'
POPUP_COMPENSATE_HELP = (
    f'为所选模型选择适当的音量补偿。\n'
    f'提醒：{COMPENSATE_HELP}'
)
VR_MODEL_PARAM_HELP = '选择运行所选模型所需的参数。'
CHOSEN_ENSEMBLE_HELP = (
    '默认集成选择：\n'
    '• 保存当前集成配置。\n'
    '• 清除所有选中的模型。\n'
    '注意：您也可以选择之前保存的集成。'
)
CHOSEN_PROCESS_METHOD_HELP = (
    '选择处理方法：\n'
    '从各种 AI 网络和算法中选择来处理您的音轨：\n'
    '\n'
    '• VR 架构：使用幅度频谱进行源分离。\n'
    '• MDX-Net：采用混合频谱网络进行源分离。\n'
    '• Demucs v3：同样使用混合频谱网络进行源分离。\n'
    '• 集成模式：结合多个模型和网络的结果以获得最佳效果。\n'
    '• 音频工具：附加实用程序以提供更多便利。'
)        

INPUT_FOLDER_ENTRY_HELP = (
    '选择输入：\n'
    '选择您要处理的音频文件。'
)
INPUT_FOLDER_ENTRY_HELP_2 = (
    '输入选项菜单：\n'
    '单击以访问输入选项菜单。'
)
OUTPUT_FOLDER_ENTRY_HELP = (
    '选择输出：\n'
    '选择将保存处理后文件的目录。'
)
INPUT_FOLDER_BUTTON_HELP = (
    '打开输入文件夹按钮：\n'
    '打开包含所选输入音频文件的目录。'
)
OUTPUT_FOLDER_BUTTON_HELP = (
    '打开输出文件夹按钮：\n'
    '打开所选输出文件夹。'
)
CHOOSE_MODEL_HELP = (
    '每种处理方法都有自己的一组选项和模型。\n'
    '在此处选择与所选处理方法关联的模型。'
)
FORMAT_SETTING_HELP = '输出保存为：'
SECONDARY_MODEL_ACTIVATE_HELP = (
    '启用后，应用将使用上面选择的模型执行额外的推理。'
)
SECONDARY_MODEL_HELP = (
    '选择辅助模型：\n'
    '选择与您希望使用当前方法处理的音轨关联的辅助模型。'
)

INPUT_SEC_FIELDS_HELP = (
    '右键单击此处选择您的输入！'
)

SECONDARY_MODEL_SCALE_HELP = ('该比例决定了主模型和辅助模型之间最终音频输出的平均方式。\n\n例如：\n\n'
                             '• 10% - 主模型结果的 10% 将计入最终结果。\n'
                             '• 50% - 主模型和辅助模型的结果将平均平均。\n'
                             '• 90% - 主模型结果的 90% 将计入最终结果。')
PRE_PROC_MODEL_ACTIVATE_HELP = (
    '启用后，应用将使用所选模型分离伴奏音轨。\n'
    '随后，所有非人声音轨将从生成的伴奏中提取。\n'
    '\n'
    '关键点：\n'
    '• 此功能可以显著减少非人声音轨中的人声泄漏。\n'
    '• 仅在 Demucs 工具中可用。\n'
    '• 仅与非人声和非伴奏音轨输出兼容。\n'
    '• 预计总处理时间会增加。\n'
    '• 只能选择 VR 或 MDX-Net 人声伴奏/人声模型用于此过程。'
)
      
AUDIO_TOOLS_HELP = (
    '从各种音频工具中选择来处理您的音轨：\n'
    '\n'
    '• 手动集成：需要选择 2 个或更多文件作为输入。这允许使用集成模式中的算法处理音轨。\n'
    '• 时间拉伸：调整所选输入的播放速度，使其更快或更慢。\n'
    '• 改变音高：修改所选输入的音高。\n'
    '• 对齐输入：选择 2 个音频文件，应用将对齐它们并提供对齐差异。\n'
    '    - 此工具提供与“Utagoe”类似的功能。\n'
    '    - 主音频：通常是混合音。\n'
    '    - 副音频：通常是伴奏。\n'
    '• 匹配处理：选择 2 个音频文件。匹配处理算法将使目标音频具有与参考音频相同的 RMS、FR、峰值幅度和立体声宽度。'
)
             
PRE_PROC_MODEL_INST_MIX_HELP = '启用后，应用将生成没有所选音轨和人声的第三个输出。'         
MODEL_SAMPLE_MODE_HELP = ('允许用户仅处理音轨的一部分，以采样设置或模型，而无需运行完整转换。\n\n注意：\n\n'
                         '• 括号中的数字是当前生成的样本的秒数。\n'
                         '• 您可以在“附加设置”菜单中选择要从音轨中提取的秒数。')
                    
POST_PROCESS_THREASHOLD_HELP = ('允许用户控制 Post_process 选项的强度。\n\n注意：\n\n'
                               '• 较高的值可能会移除更多伪影，但泄漏可能会增加。\n'
                               '• 较低的值限制伪影的移除。')

BATCH_SIZE_HELP = ('指定一次处理的批次数。\n\n注意：\n\n'
                               '• 较高的值意味着更多的 RAM 使用，但处理时间稍快。\n'
                               '• 较低的值意味着较少的 RAM 使用，但处理时间稍长。\n'
                               '• 批量大小值对输出质量没有影响。')
         
VR_MODEL_NOUT_HELP = ""
VR_MODEL_NOUT_LSTM_HELP = ""
  
IS_PHASE_HELP = '选择副音频的相位。\n• 注意：强烈建议使用“自动”选项。'
IS_ALIGN_TRACK_HELP = '启用此选项以在对齐后保存副音轨。'
IS_MATCH_SILENCE_HELP = (
    '将副音频的初始静音与主音频对齐。\n'
    '• 注意：如果主音频仅以人声开头，请避免使用此选项。'
)
IS_MATCH_SPEC_HELP = '基于主音频的频谱对齐副音频。\n• 注意：这可能会改善特定情况下的对齐。'

TIME_WINDOW_ALIGN_HELP = (
                           '此设置确定对齐分析的窗口大小，特别适用于存在微小时间差异的音频对：\n'
                           '\n'
                           '• 无：禁用时间窗口分析。\n'
                           '• 1：按 0.0625 秒窗口分析对。\n'
                           '• 2：按 0.125 秒窗口分析对。\n'
                           '• 3：按 0.25 秒窗口分析对。\n'
                           '• 4：按 0.50 秒窗口分析对。\n'
                           '• 5：按 0.75 秒窗口分析对。\n'
                           '• 6：按 1 秒窗口分析对。\n'
                           '• 7：按 2 秒窗口分析对。\n'
                           '\n'
                           '偏移选项：\n'
                           '• 低：循环通过 0.0625 和 0.5 秒窗口以找到最佳匹配。\n'
                           '• 中：循环通过 0.0625、0.125 和 0.5 秒窗口以找到最佳匹配。\n'
                           '• 高：循环通过 0.0625、0.125、0.25 和 0.5 秒窗口以找到最佳匹配。\n'
                           '\n'
                           '需要考虑的要点：\n'
                           '    - 使用“偏移”选项可能需要更多处理时间，并且可能无法保证更好的结果。\n'
                           '    - 选择较小的分析窗口会增加处理时间。\n'
                           '    - 最佳设置可能因具体处理的音轨而异。'
)
INTRO_ANALYSIS_ALIGN_HELP = (
                           '此设置确定要分析的音频输入部分以进行初始对齐。\n'
                           '\n'
                           '• 默认：分析音频总长度的 10%（或 1/10）。\n'
                           '• 1：分析音频总长度的 12.5%（或 1/8）。\n'
                           '• 2：分析音频总长度的 16.67%（或 1/6）。\n'
                           '• 3：分析音频总长度的 25%（或 1/4）。\n'
                           '• 4：分析音频总长度的 50%（或一半）。\n'
                           '\n'
                           '偏移选项：\n'
                           '• 低：循环通过 2 个前奏分析值。\n'
                           '• 中：循环通过 3 个前奏分析值。\n'
                           '• 高：循环通过 5 个前奏分析值。\n'
                           '\n'
                           '需要考虑的要点：\n'
                           '    - 使用“偏移”选项将需要更多处理时间，并且可能无法保证更好的结果。\n'
                           '    - 最佳设置可能因具体处理的音轨而异。'
)

VOLUME_ANALYSIS_ALIGN_HELP = (
                           '此设置指定要对副输入进行的音量调整：\n'
                           '\n'
                           '• 无：不进行音量调整。\n'
                           '• 低：在 4dB 范围内分析音频，以 1dB 为增量进行调整。\n'
                           '• 中：在 6dB 范围内分析音频，以 1dB 为增量进行调整。\n'
                           '• 高：在 6dB 范围内分析音频，以 0.5dB 为增量进行调整。\n'
                           '• 非常高：在 10dB 范围内分析音频，以 0.5dB 为增量进行调整。\n'
                           '\n'
                           '需要考虑的要点：\n'
                           '    - 选择更广泛的分析选项（例如，高、非常高）将导致更长的处理时间。\n'
                           '    - 最佳设置可能因具体处理的音轨而异。'
)

PHASE_SHIFTS_ALIGN_HELP = (
                           '此设置指定要对副输入进行的相位调整：\n'
                           '\n'
                           '偏移选项：\n'
                           '• 无：不进行相位调整。\n'
                           '• 非常低：在 2 个不同相位位置的范围内分析音频。\n'
                           '• 低：在 4 个不同相位位置的范围内分析音频。\n'
                           '• 中：在 8 个不同相位位置的范围内分析音频。\n'
                           '• 高：在 18 个不同相位位置的范围内分析音频。\n'
                           '• 非常高：在 36 个不同相位位置的范围内分析音频。\n'
                           '• 最大：在所有 360 个相位位置分析音频。\n'
                           '\n'
                           '需要考虑的要点：\n'
                           '    - 此选项仅适用于时间校正。\n'
                           '    - 如果其中一个输入来自模拟源，此选项可能会有所帮助。\n'
                           '    - 选择更广泛的分析选项（例如，高、非常高）将导致更长的处理时间。\n'
                           '    - 选择“最大”可能需要数小时才能处理。\n'
                           '    - 最佳设置可能因具体处理的音轨而异。'
)

# Warning Messages
STORAGE_ERROR = '存储空间不足', '主驱动器上没有足够的存储空间来继续。您的主驱动器必须至少有 3 GB 的存储空间才能让此应用正常运行。\n\n请确保您的主驱动器至少有 3 GB 的存储空间，然后重试。\n\n'
STORAGE_WARNING = '可用存储空间低', '您的主驱动器存储空间不足。您的主驱动器必须至少有 3 GB 的存储空间才能让此应用正常运行。\n\n'
CONFIRM_WARNING = '\n您确定要继续吗？'
PROCESS_FAILED = '处理失败，请查看错误日志\n'
EXIT_PROCESS_ERROR = '活动进程', '请停止活动进程或等待其完成后再退出。'
EXIT_HALTED_PROCESS_ERROR = '正在停止进程', '请等待应用完成停止进程后再退出。'
EXIT_DOWNLOAD_ERROR = '活动下载', '请停止下载或等待其完成后再退出。'
SET_TO_DEFAULT_PROCESS_ERROR = '活动进程', '在活动进程期间不能重置所有应用设置。'
SET_TO_ANY_PROCESS_ERROR = '活动进程', '在活动进程期间不能重置应用设置。'
RESET_ALL_TO_DEFAULT_WARNING = '重置设置确认', '所有应用设置将恢复为出厂默认设置。\n\n您确定要继续吗？'
AUDIO_VERIFICATION_CHECK = lambda i, e:f'++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n已移除损坏文件：\n\n{i}\n\n错误详情：\n\n{e}\n++++++++++++++++++++++++++++++++++++++++++++++++++++'
INVALID_ONNX_MODEL_ERROR = '无效模型', '所选文件不是有效的 MDX-Net 模型。请查看错误日志以获取更多信息。'
INVALID_PARAM_MODEL_ERROR = '选择模型参数', '请选择一个模型参数或单击“取消”。'
UNRECOGNIZED_MODEL = '检测到未识别模型', ' 是一个未识别的模型。\n\n' + \
                     '您是否希望在继续之前选择正确的参数？'
STOP_PROCESS_CONFIRM = '确认', '您即将停止所有活动进程。\n\n您确定要继续吗？'
NO_ENSEMBLE_SELECTED = '未选择模型', '请选择集成并重试。'
PICKLE_CORRU = '文件损坏', '无法加载此集成。\n\n' + \
               '您是否希望将此集成从列表中移除？'
DELETE_ENS_ENTRY = '确认移除', '您确定要移除此条目吗？'

# Separation Text
LOADING_MODEL = '正在加载模型...'
INFERENCE_STEP_1 = '正在运行推理...'
INFERENCE_STEP_1_SEC = '正在运行推理（辅助模型）...'
INFERENCE_STEP_1_4_STEM = lambda stem:f'正在运行推理（{stem} 的辅助模型）...'
INFERENCE_STEP_1_PRE = '正在运行推理（预处理模型）...'
INFERENCE_STEP_1_VOC_S = '正在分离人声...'
INFERENCE_STEP_2_PRE = lambda pm, m:f'正在加载预处理模型（{pm}：{m}）...'
INFERENCE_STEP_2_SEC = lambda pm, m:f'正在加载辅助模型（{pm}：{m}）...'
INFERENCE_STEP_2_VOC_S = lambda pm, m:f'正在加载人声分离器模型（{pm}：{m}）...'
INFERENCE_STEP_2_SEC_CACHED_MODOEL = lambda pm, m:f'辅助模型（{pm}：{m}）缓存已加载。\n'
INFERENCE_STEP_2_PRE_CACHED_MODOEL = lambda pm, m:f'预处理模型（{pm}：{m}）缓存已加载。\n'
INFERENCE_STEP_2_SEC_CACHED = '正在加载缓存的辅助模型源... 完成！\n'
INFERENCE_STEP_2_PRIMARY_CACHED = ' 模型缓存已加载。\n'
INFERENCE_STEP_2 = '推理完成。'
INFERENCE_STEP_DEVERBING = ' 正在去混响...'
SAVING_STEM = '正在保存 ', ' 音轨...'
SAVING_ALL_STEMS = '正在保存所有音轨...'
ENSEMBLING_OUTPUTS = '正在集成输出...'
DONE = ' 完成！\n'
ENSEMBLES_SAVED = '集成输出已保存！\n\n'

#Additional Text
CHOOSE_PROC_METHOD_MAIN_LABEL = '选择处理方法'
SELECT_SAVED_SETTINGS_MAIN_LABEL = '选择已保存的设置'
CHOOSE_MDX_MODEL_MAIN_LABEL = '选择 MDX-NET 模型'
BATCHES_MDX_MAIN_LABEL = '批量大小'
VOL_COMP_MDX_MAIN_LABEL = '音量补偿'
SEGMENT_MDX_MAIN_LABEL = '段大小'
SELECT_VR_MODEL_MAIN_LABEL = '选择 VR 模型'
AGGRESSION_SETTING_MAIN_LABEL = '侵略性设置'
WINDOW_SIZE_MAIN_LABEL = '窗口大小'
CHOOSE_DEMUCS_MODEL_MAIN_LABEL = '选择 DEMUCS 模型'
CHOOSE_STEMS_MAIN_LABEL = '选择音轨'
CHOOSE_SEGMENT_MAIN_LABEL = '段'
ENSEMBLE_OPTIONS_MAIN_LABEL = '集成选项'
CHOOSE_MAIN_PAIR_MAIN_LABEL = '主音轨对'
CHOOSE_ENSEMBLE_ALGORITHM_MAIN_LABEL = '集成算法'
AVAILABLE_MODELS_MAIN_LABEL = '可用模型'
CHOOSE_AUDIO_TOOLS_MAIN_LABEL = '选择音频工具'
CHOOSE_MANUAL_ALGORITHM_MAIN_LABEL = '选择算法'
CHOOSE_RATE_MAIN_LABEL = '速率'
CHOOSE_SEMITONES_MAIN_LABEL = '半音'
GPU_CONVERSION_MAIN_LABEL = 'GPU 转换'
CHANGE_LOG_HEADER = lambda patch:f"补丁版本：\n\n{patch}"
INVALID_INPUT_E = ' 无效输入！ '
LB_UP = "上移选择"
LB_DOWN = "下移选择"
LB_CLEAR = "清空框"
LB_MOVE_OVER_P = "将选择移至副列表"
LB_MOVE_OVER_S = "将选择移至主列表"
FILE_ONE_MAIN_LABEL = "主音频"
FILE_TWO_MAIN_LABEL = "副音频"
FILE_ONE_MATCH_MAIN_LABEL = "目标音频"
FILE_TWO_MATCH_MAIN_LABEL = "参考音频"
TIME_WINDOW_MAIN_LABEL = "时间调整"
INTRO_ANALYSIS_MAIN_LABEL = "前奏分析"
VOLUME_ADJUSTMENT_MAIN_LABEL = "音量调整"
SELECT_INPUTS = "选择输入"
SELECTED_INPUTS = '已选输入'
WIDEN_BOX = '加宽框'
CONFIRM_ENTRIES = '确认条目'
CLOSE_WINDOW = '关闭窗口'
DUAL_AUDIO_PROCESSING = '双音频批量处理'
CANCEL_TEXT = "取消"
CONFIRM_TEXT = "确认"
SELECT_MODEL_TEXT = '选择模型'
NONE_SELECTED = '未选择'
SAVE_TEXT = '保存'
OVERLAP_TEXT = '重叠'
ACCEPT_ANY_INPUT_TEXT = '接受任何输入'
ACTIVATE_PRE_PROCESS_MODEL_TEXT = '激活预处理模型'
ACTIVATE_SECONDARY_MODEL_TEXT = '激活辅助模型'
ADDITIONAL_MENUS_INFORMATION_TEXT = '附加菜单和信息'
ADDITIONAL_SETTINGS_TEXT = '附加设置'
ADVANCED_ALIGN_TOOL_OPTIONS_TEXT = '高级对齐工具选项'
ADVANCED_DEMUCS_OPTIONS_TEXT = '高级 Demucs 选项'
ADVANCED_ENSEMBLE_OPTIONS_TEXT = '高级集成选项'
ADVANCED_MDXNET23_OPTIONS_TEXT = '高级 MDX-NET23 选项'
ADVANCED_MDXNET_OPTIONS_TEXT = '高级 MDX-Net 选项'
ADVANCED_OPTION_MENU_TEXT = '高级选项菜单'
ADVANCED_VR_OPTIONS_TEXT = '高级 VR 选项'
AGGRESSION_SETTING_TEXT = '侵略性设置'
APPEND_ENSEMBLE_NAME_TEXT = '附加集成名称'
APPLICATION_DOWNLOAD_CENTER_TEXT = '应用下载中心'
APPLICATION_UPDATES_TEXT = '应用更新'
AUDIO_FORMAT_SETTINGS_TEXT = '音频格式设置'
BALANCE_VALUE_TEXT = '平衡值'
BATCH_SIZE_TEXT = '批量大小'
BV_MODEL_TEXT = 'BV 模型'
CHANGE_MODEL_DEFAULT_TEXT = '更改模型默认值'
CHANGE_MODEL_DEFAULTS_TEXT = '更改模型默认值'
CHANGE_PARAMETERS_TEXT = '更改参数'
CHOOSE_ADVANCED_MENU_TEXT = '选择高级菜单' 
CHOOSE_MODEL_PARAM_TEXT = '选择模型参数'
CLEAR_AUTOSET_CACHE_TEXT = '清除自动设置缓存'
COMBINE_STEMS_TEXT = '组合音轨'
CONFIRM_UPDATE_TEXT = '确认更新'
COPIED_TEXT = '已复制！'
COPY_ALL_TEXT_TEXT = '复制所有文本'
DEFINED_PARAMETERS_DELETED_TEXT = '已定义的参数已删除'
DELETE_PARAMETERS_TEXT = '删除参数'
DELETE_USER_SAVED_SETTING_TEXT = '删除用户保存的设置'
DEMUCS_TEXT = 'Demucs'
DENOISE_OUTPUT_TEXT = '降噪输出'
DEVERB_VOCALS_TEXT = '去混响人声'
DONE_TEXT = '完成'
DOWNLOAD_CENTER_TEXT = '下载中心'
DOWNLOAD_CODE_TEXT = '下载代码'
DOWNLOAD_LINKS_TEXT = '下载链接'
DOWNLOAD_UPDATE_IN_APPLICATION_TEXT = '在应用中下载更新'
ENABLE_HELP_HINTS_TEXT = '启用帮助提示'
ENABLE_TTA_TEXT = '启用 TTA'
ENABLE_VOCAL_SPLIT_MODE_TEXT = '启用人声分离模式'
ENSEMBLE_NAME_TEXT = '集成名称'
ENSEMBLE_WAVFORMS_TEXT = '集成波形'
ERROR_CONSOLE_TEXT = '错误控制台'
GENERAL_MENU_TEXT = '常规菜单'
GENERAL_PROCESS_SETTINGS_TEXT = '常规处理设置'
GENERATE_MODEL_FOLDER_TEXT = '生成模型文件夹'
HIGHEND_PROCESS_TEXT = '高端处理'
INPUT_CODE_TEXT = '输入代码'
INPUT_STEM_NAME_TEXT = '输入音轨名称'
INPUT_UNIQUE_STEM_NAME_TEXT = '输入唯一音轨名称'
IS_INVERSE_STEM_TEXT = '是否反相音轨'
KARAOKE_MODEL_TEXT = '卡拉 OK 模型'
MANUAL_DOWNLOADS_TEXT = '手动下载'
MATCH_FREQ_CUTOFF_TEXT = '匹配频率截止'
MDXNET_C_MODEL_PARAMETERS_TEXT = 'MDX-Net C 模型参数'
MDXNET_MODEL_SETTINGS_TEXT = 'MDX-Net 模型设置'
MDXNET_TEXT = 'MDX-Net'
MODEL_PARAMETERS_CHANGED_TEXT = '模型参数已更改'
MODEL_SAMPLE_MODE_SETTINGS_TEXT = '模型样本模式设置'
MODEL_TEST_MODE_TEXT = '模型测试模式'
MP3_BITRATE_TEXT = 'Mp3 比特率'
NAME_SETTINGS_TEXT = '名称设置'
NO_DEFINED_PARAMETERS_FOUND_TEXT = '未找到已定义的参数'
NO_TEXT = '否'
NORMALIZE_OUTPUT_TEXT = '归一化输出'
USE_OPENCL_TEXT = '使用 OpenCL'
NOT_ENOUGH_MODELS_TEXT = '模型不足'
NOTIFICATION_CHIMES_TEXT = '通知提示音'
OPEN_APPLICATION_DIRECTORY_TEXT = '打开应用目录'
OPEN_LINK_TO_MODEL_TEXT = '打开模型链接'
OPEN_MODEL_DIRECTORY_TEXT = '打开模型目录'
OPEN_MODEL_FOLDER_TEXT = '打开模型文件夹'
OPEN_MODELS_FOLDER_TEXT = '打开模型文件夹'
PHASE_SHIFTS_TEXT = '相位偏移'
POST_PROCESS_TEXT = '后处理'
POST_PROCESS_THRESHOLD_TEXT = '后处理阈值'
PREPROCESS_MODEL_CHOOSE_TEXT = '预处理模型'
PRIMARY_STEM_TEXT = '主音轨'
REFRESH_LIST_TEXT = '刷新列表'
REMOVE_SAVED_ENSEMBLE_TEXT = '移除已保存的集成'
REPORT_ISSUE_TEXT = '报告问题'
RESET_ALL_SETTINGS_TO_DEFAULT_TEXT = '重置所有设置为默认'
RESTART_APPLICATION_TEXT = '重启应用'
SAMPLE_CLIP_DURATION_TEXT = '样本片段时长'
SAVE_ALIGNED_TRACK_TEXT = '保存对齐音轨'
SAVE_ALL_OUTPUTS_TEXT = '保存所有输出'
SAVE_CURRENT_ENSEMBLE_TEXT = '保存当前集成'
SAVE_CURRENT_SETTINGS_TEXT = '保存当前设置'
SAVE_INSTRUMENTAL_MIXTURE_TEXT = '保存伴奏混合'
SAVE_SPLIT_VOCAL_INSTRUMENTALS_TEXT = '保存分离人声伴奏'
SECONDARY_MODEL_TEXT = '辅助模型'
SECONDARY_PHASE_TEXT = '副相位'
SECONDS_TEXT = '秒'
SEGMENT_DEFAULT_TEXT = '段默认'
SEGMENT_SIZE_TEXT = '段大小'
SEGMENTS_TEXT = '段'
SELECT_DOWNLOAD_TEXT = '选择下载'
SELECT_MODEL_PARAM_TEXT = '选择模型参数'
SELECT_VOCAL_TYPE_TO_DEVERB_TEXT = '选择要去除混响的人声类型'
SELECTED_MODEL_PLACEMENT_PATH_TEXT = '所选模型放置路径'
SETTINGS_GUIDE_TEXT = '设置指南'
SETTINGS_TEST_MODE_TEXT = '设置测试模式'
SHIFT_CONVERSION_PITCH_TEXT = '偏移转换音高'
SHIFTS_TEXT = '偏移'
SILENCE_MATCHING_TEXT = '静音匹配'
SPECIFY_MDX_NET_MODEL_PARAMETERS_TEXT = '指定 MDX-Net 模型参数'
SPECIFY_PARAMETERS_TEXT = '指定参数'
SPECIFY_VR_MODEL_PARAMETERS_TEXT = '指定 VR 模型参数'
SPECTRAL_INVERSION_TEXT = '频谱反相'
SPECTRAL_MATCHING_TEXT = '频谱匹配'   
SPLIT_MODE_TEXT = '分割模式'
STEM_NAME_TEXT = '音轨名称'
STOP_DOWNLOAD_TEXT = '停止下载'
SUPPORT_UVR_TEXT = '支持 UVR'
TRY_MANUAL_DOWNLOAD_TEXT = '尝试手动下载'
UPDATE_FOUND_TEXT = '发现更新'
USER_DOWNLOAD_CODES_TEXT = '用户下载代码'
UVR_BUY_ME_A_COFFEE_LINK_TEXT = 'UVR “Buy Me a Coffee” 链接'
UVR_ERROR_LOG_TEXT = 'UVR 错误日志'
UVR_PATREON_LINK_TEXT = 'UVR Patreon 链接'
VOCAL_DEVERB_OPTIONS_TEXT = '人声去混响选项'
VOCAL_SPLIT_MODE_OPTIONS_TEXT = '人声分离模式选项'
VOCAL_SPLIT_OPTIONS_TEXT = '人声分离选项'
VOLUME_COMPENSATION_TEXT = '音量补偿'
VR_51_MODEL_TEXT = 'VR 5.1 模型'
VR_ARCH_TEXT = 'VR 架构'
WAV_TYPE_TEXT = 'WAV 类型'
CUDA_NUM_TEXT = 'GPU 设备'
WINDOW_SIZE_TEXT = '窗口大小'
YES_TEXT = '是'
VERIFY_INPUTS_TEXT = '验证输入'
AUDIO_INPUT_TOTAL_TEXT = '音频输入总数'
MDX23C_ONLY_OPTIONS_TEXT = '仅 MDXNET23 选项'
PROCESS_STARTING_TEXT = '进程启动中... '
MISSING_MESS_TEXT = '缺失或损坏。'
SIMILAR_TEXT = "相同。"
LOADING_VERSION_INFO_TEXT = '正在加载版本信息...'
CHECK_FOR_UPDATES_TEXT = '检查更新'
INFO_UNAVAILABLE_TEXT = "信息不可用。"
UPDATE_CONFIRMATION_TEXT = '您确定要继续吗？\n\n应用将需要重新启动。\n'
BROKEN_OR_INCOM_TEXT = '已移除损坏或不兼容的文件。请查看错误日志了解详情。'
BMAC_UVR_TEXT = 'UVR “Buy Me a Coffee” 链接'
MDX_MENU_WAR_TEXT = '（如果不确定，请保持此设置不变。）'
NO_FILES_TEXT = '无文件'
CHOOSE_INPUT_TEXT = '选择输入'
OPEN_INPUT_DIR_TEXT = '打开输入目录'
BATCH_PROCESS_MENU_TEXT = '批处理菜单'
TEMP_FILE_DELETION_TEXT = '临时文件删除'
VOCAL_SPLITTER_OPTIONS_TEXT = '人声分离器选项'
WAVEFORM_ENSEMBLE_TEXT = '波形集成'
SELECT_INPUT_TEXT = '选择输入'
SELECT_OUTPUT_TEXT = '选择输出'
TIME_CORRECTION_TEXT = '时间校正'
UVR_LIS_INFO_TEXT = 'UVR 许可证信息'
ADDITIONAL_RES_CREDITS_TEXT = '附加资源和致谢'
SAVE_INST_MIXTURE_TEXT = '保存伴奏混合'
DOWNLOAD_UPDATE_IN_APP_TEXT = '在应用中下载更新'
WAVE_TYPE_TEXT = '波形类型'
OPEN_LINK_TO_MODEL_TEXT = "打开模型链接"
OPEN_MODEL_DIRECTORY = "打开模型目录"
SELECTED_MODEL_PLACE_PATH_TEXT = '所选模型放置路径'
IS_INVERSE_STEM_TEXT = "是否反相音轨"
INPUT_STEM_NAME_TEXT = "输入音轨名称"
INPUT_UNIQUE_STEM_NAME_TEXT = "输入唯一音轨名称"
DONE_MENU_TEXT = "完成"
OK_TEXT = "确定"
ENSEMBLE_WARNING_NOT_ENOUGH_SHORT_TEXT = "模型不足"
ENSEMBLE_WARNING_NOT_ENOUGH_TEXT = "您必须选择 2 个或更多模型才能保存集成。"
NOT_ENOUGH_ERROR_TEXT = "文件数量不足，无法处理。\n"
INVALID_FOLDER_ERROR_TEXT = '无效文件夹', '您提供的导出路径不是有效的文件夹！'

GET_DL_VIP_CODE_TEXT = ("通过访问以下链接之一获取代码。"
                        "\n在那里您可以捐赠、承诺，"
                        "或直接获取代码！\n（不需要捐赠即可获得 VIP 代码）")
CONFIRM_RESTART_TEXT = '重启确认', '这将重启应用并停止所有正在运行的进程。您当前的设置将被保存。\n\n 您确定要继续吗？'
ERROR_LOADING_FILE_TEXT = '加载以下文件时出错', '原始错误详情'
LOADING_MODEL_TEXT = '正在加载模型'
FULL_APP_SET_TEXT = '完整应用设置'
PROCESS_STARTING_TEXT = '进程启动中... '
PROCESS_STOPPED_BY_USER = '\n\n用户已停止进程。'
NEW_UPDATE_FOUND_TEXT = lambda version:f"\n\n发现新更新：{version}\n\n单击“设置”菜单中的更新按钮以下载并安装！"
ROLL_BACK_TEXT = '单击此处回滚'

def secondary_stem(stem:str):
    """Determines secondary stem"""
    
    stem = stem if stem else NO_STEM
    
    if stem in STEM_PAIR_MAPPER.keys():
        for key, value in STEM_PAIR_MAPPER.items():
            if stem in key:
                secondary_stem = value
    else:
        secondary_stem = stem.replace(NO_STEM, "") if NO_STEM in stem else f"{NO_STEM}{stem}"
    
    return secondary_stem
