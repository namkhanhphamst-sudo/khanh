import streamlit as st
import math

# ==========================================
# CẤU HÌNH TRANG WEB HOÀNG GIA
# ==========================================
st.set_page_config(
    page_title="Trạm Xuất Quân Định Lượng - khanhsteve", 
    page_icon="⚔️", 
    layout="centered"
)

# ==========================================
# CỔNG BẢO MẬT ĐẾ VƯƠNG (CÓ CƠ CHẾ TÀNG HÌNH)
# ==========================================
MAT_KHAU_CHAN_MENH = "chanmenh2026"

# Tạo một cái khung chứa Cổng đăng nhập
khung_dang_nhap = st.empty()

with khung_dang_nhap.container():
    st.title("🛡️ CỔNG BẢO MẬT ĐẾ VƯƠNG")
    nhap_mat_khau = st.text_input(">> Khai báo Mật danh để kích hoạt Lò phản ứng:", type="password")

    if nhap_mat_khau != MAT_KHAU_CHAN_MENH:
        if nhap_mat_khau:
            st.error("❌ Mật danh sai! Cảnh báo kẻ xâm nhập: Rời khỏi đây ngay lập tức!")
        
        st.divider()
        col_logo_uet, col_text_khanh = st.columns([1, 3])
        with col_logo_uet:
            st.image("https://raw.githubusercontent.com/anhducusth/uet-logo/main/logo_uet.png", width=70) 
        with col_text_khanh:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 🏛️ UET - ĐẠI HỌC CÔNG NGHỆ")
            st.markdown("<p style='color: gray; font-style: italic;'>An ninh được thiết lập bởi khanhsteve</p>", unsafe_allow_html=True)
        
        # Chặn toàn bộ code bên dưới nếu chưa nhập đúng pass
        st.stop()

# NẾU NHẬP ĐÚNG PASS: Lệnh này sẽ xóa sạch cái ô nhập mật khẩu đi
khung_dang_nhap.empty()

# ==========================================
# GIAO DIỆN CHÍNH (SAU KHI ĐÃ ĐĂNG NHẬP THÀNH CÔNG)
# ==========================================

# --- THANH BÊN (SIDEBAR) ---
with st.sidebar:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/anhducusth/uet-logo/main/logo_uet.png", width=120)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>UET - VNU</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Đại học Công nghệ - ĐHQGHN</p>", unsafe_allow_html=True)
    st.divider()
    
    st.markdown("<div style='text-align: center; margin-top: 20px; padding: 10px; border: 2px solid #1E3A8A; border-radius: 10px; background-color: #F0F9FF;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin: 0; color: #1E3A8A;'>⚔️ MADE BY</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin: 0; color: #1E3A8A; font-family: monospace;'>khanhsteve</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin: 0; color: gray;'>Quân sư Định lượng Cấp cao</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Phiên bản độc quyền 2026</p>", unsafe_allow_html=True)

# --- BẢN GIAO HƯỞNG NHỊ PHÂN (ĐÃ ĐỔI LINK ẢNH KHÔNG BỊ RÁCH) ---
st.image("https://media.giphy.com/media/xTiTnxpQ3ghPiB2Hp6/giphy.gif", use_container_width=True)
st.markdown("<p style='text-align: center; color: #00FF00; font-family: monospace; font-size: 14px; letter-spacing: 2px;'>BINARY SYSTEM VISUAL - POWERED BY KHANHSTEVE</p>", unsafe_allow_html=True)

st.title("⚔️ TRẠM XUẤT QUÂN ĐỊNH LƯỢNG")
st.markdown("Hệ thống phân bổ vốn chuẩn The5ers")
st.divider()

# --- LÕI TOÁN HỌC ---
def co_may_tu_do(ngan_kho, rui_ro_pt, gia_vao, gia_sl, contract_size, commission_1_lot, chu_so_thap_phan, swap_points, dem_ngam, dem_x3):
    tien_rui_ro_toi_da = ngan_kho * (rui_ro_pt / 100)
    khoang_cach_gia = round(abs(gia_vao - gia_sl), 5)
    
    if khoang_cach_gia == 0:
        return 0.0, 0.0, 0.0, tien_rui_ro_toi_da, 0.0, 0.0
        
    tien_mat_gia_1_lot = khoang_cach_gia * contract_size
    point_size = 10 ** (-chu_so_thap_phan)
    
    swap_usd_1_dem = swap_points * point_size * contract_size
    dem_thuong = dem_ngam - dem_x3
    tong_swap_1_lot = (swap_usd_1_dem * dem_thuong) + (swap_usd_1_dem * 3 * dem_x3) 
    
    chi_phi_1_lot = tien_mat_gia_1_lot + commission_1_lot + tong_swap_1_lot
    
    lot_size_tho = tien_rui_ro_toi_da / chi_phi_1_lot
    lot_chinh_xac = math.floor(lot_size_tho * 100 + 1e-9) / 100.0 
    
    thiet_hai_thuc_te = round(lot_chinh_xac * chi_phi_1_lot, 2)
    return lot_chinh_xac, thiet_hai_thuc_te, khoang_cach_gia, tien_rui_ro_toi_da, chi_phi_1_lot, round(tong_swap_1_lot, 2)

# --- BẢNG ĐIỀU KHIỂN CHIẾN LƯỢC ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Tọa Độ & Ngân Khố")
    nk = st.number_input("Ngân khố (USD)", min_value=1.0, value=2500.0, step=100.0)
    rr = st.number_input("Rủi ro (% tài khoản)", min_value=0.1, value=1.75, step=0.1)
    gv = st.number_input("Giá Vào Lệnh (Entry)", value=71070.0, format="%.5f")
    sl = st.number_input("Giá Cắt Lỗ (Stop Loss)", value=70800.0, format="%.5f")

with col2:
    st.subheader("2. Thông Số Sàn MT5")
    cs = st.number_input("Contract Size", min_value=1.0, value=1.0)
    com = st.number_input("Phí Commission 1 Lot ($)", min_value=0.0, value=8.0)
    chu_so = st.number_input("Digits (Chữ số thập phân)", min_value=0, value=2)
    swap = st.number_input("Số Điểm Swap bị trừ", value=1358.9)
    dem = st.number_input("Tổng số đêm ngâm lệnh", min_value=0, value=0)
    t_x3 = st.number_input("Số đêm bị nhân 3 Swap", min_value=0, value=0)

st.divider()

if st.button("🔥 TÍNH TOÁN XUẤT QUÂN 🔥", use_container_width=True):
    lot, thiet_hai, kc_gia, tran_rui_ro, chi_phi_1_lot, tong_swap = co_may_tu_do(nk, rr, gv, sl, cs, com, chu_so, swap, dem, t_x3)
    
    st.subheader("BÁO CÁO TOÁN HỌC")
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Khoảng cách Cắt lỗ", value=f"{kc_gia} Giá")
    m2.metric(label="Hạn mức rủi ro", value=f"${tran_rui_ro}")
    m3.metric(label="Thuế Swap (1 Lot)", value=f"${tong_swap}")
    
    st.markdown("---")
    
    if lot < 0.01:
        chi_phi_toi_thieu = round(chi_phi_1_lot * 0.01, 2)
        st.error("🚨 GIAO THỨC BÁO ĐỘNG ĐỎ KÍCH HOẠT: Cấm vào lệnh!")
        st.warning(f"Khoảng cách Cắt lỗ quá xa. Để đánh nhỏ nhất 0.01 Lot, ngài sẽ mất {chi_phi_toi_thieu} USD.")
    else:
        st.success(f"✅ LỆNH VUNG KIẾM: ĐÁNH CHÍNH XÁC {lot} LOT")
        st.info(f"🩸 Tổng thiệt hại nếu chạm SL: {thiet_hai} USD (Đã gồm phí)")
