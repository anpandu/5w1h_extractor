
dtext = 'San Francisco (ANTARA News) - Oracle Corp merilis update keamanan komputer Selasa waktu AS untuk versi program Java yang berlaku dalam browser Web agar lebih sulit dibajak peretas. 42 lubang kerentanan dalam Java ini termasuk mayoritas dari yang sebelum ini dianggap paling kritis, kata Wakil Presiden Eksekutif Oracle Hasan Rizvi seperti dikutip Reuters. Tahun lalu, serangkaian lubang keamanan besar dalam plug-in Java untuk browser telah dibobol peretas yang beberapa diantaranya dimanfaatkan kelompok kriminal sebelum bolong tersebut diketahui. Kampanye peretasan besar-besaran tahun lalu, menginfeksi komputer ber-OS Windows dari Microsoft Corp dan software Apple. Departemen Keamanan Dalam Negeri telah merekomendasikan pengguna komputer mematikan Java di browser, namun banyak perusahaan besar menggunakan software internal yang tergantung pada Java dan memaksa Oracle membuat bahasa pemrogaman itu aman. Oracle mewarisi Java saat membeli Sun Microsystems pada 2010. Itu adalah eksposur besar satu perusahaan ke pasar, saat versi Java beroperasi di desktop, telepon dan perangkat serta server lainnya. Kendati begitu versi browser secara khusus rawan dari masalah keamanan. Menurut produsen software keamanan komputer Kaspersky, tahun lalu Java melampaui software Reader dari Adobe Systems Inc sebagai bagian software yang paling sering diserang. Sepanjang tahun lalu Java menjadi wahana untuk 50 persen semua serangan siber di mana peretas membobol komputer dengan mengekpsploitasi kutu software, kata Kaspersky. Diikuti Adobe Reader dengan 28 persen dari semua insiden, sedangkan Microsoft Windows dan Internet Explorer terlibat dalam sekitar 3 persen insiden. Kendati begitu tidak ada profile konsumen Oracle yang terancam oleh masalah keamanan komputer, kata Rizvi. "Ini adalah pertarungan demi kelangsungan hidup plug-in Java. Apakah banyak perusahaan yang mematikannya atau malah percaya diri untuk memperbaikinya," kata analis IDC, Al Hilwa.'
dwhat = 'Oracle Corp merilis update keamanan komputer Selasa waktu AS untuk versi program Java yang berlaku dalam browser Web'
dwho = 'Oracle Corp'
dwhen = 'Selasa'
dwhere = 'San Francisco'
dwhy = 'agar lebih sulit dibajak peretas'
dhow = ''

function submitNews() {
	$("#info5w1hBox").css("display", "block");
	$(".paddingBox").css("display", "none");
	$("#inputNewsBox").removeClass("col-sm-10").addClass("col-sm-6");
	fill5w1h(dtext, dwhat, dwho, dwhen, dwhere, dwhy, dhow);
}

function getContent() {

}

function fill5w1h(a, b, c, d, e, f) {
	$("#inputNews").val(a)
	$("#outputWhat").val(b)
	$("#outputWho").val(c)
	$("#outputWhen").val(d)
	$("#outputWhere").val(e)
	$("#outputWhy").val(f)
	$("#outputHow").val(g)
}

