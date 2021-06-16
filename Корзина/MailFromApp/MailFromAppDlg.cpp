// MailFromAppDlg.cpp : implementation file
//

#include "stdafx.h"
#include "MailFromApp.h"
#include "MailFromAppDlg.h"
#include <winsock2.h>

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CAboutDlg dialog used for App About

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	//{{AFX_MSG(CAboutDlg)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// No message handlers
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CMailFromAppDlg dialog

CMailFromAppDlg::CMailFromAppDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CMailFromAppDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CMailFromAppDlg)
	m_sFrom = _T("");
	m_sServer = _T("");
	m_sText = _T("");
	m_sTo = _T("");
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CMailFromAppDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CMailFromAppDlg)
	DDX_Text(pDX, IDC_FROM, m_sFrom);
	DDX_Text(pDX, IDC_SERVERNAME, m_sServer);
	DDX_Text(pDX, IDC_TEXT, m_sText);
	DDX_Text(pDX, IDC_TO, m_sTo);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CMailFromAppDlg, CDialog)
	//{{AFX_MSG_MAP(CMailFromAppDlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_SEND, OnSend)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CMailFromAppDlg message handlers

BOOL CMailFromAppDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	// TODO: Add extra initialization here
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CMailFromAppDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CMailFromAppDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CMailFromAppDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CMailFromAppDlg::OnSend() 
{
	UpdateData(TRUE);

	CString Serv = "HELO " + m_sServer + "\r\n";
	CString From = "MAIL FROM:<" + m_sFrom + ">\r\n";
	CString To = "RCPT TO:<" + m_sTo + ">\r\n";
	CString Text = m_sText + "\r\n\r\n.\r\n";
	
	
	char *MailMessage[] = 
	{
		Serv.GetBuffer(1),
		From.GetBuffer(1),
		To.GetBuffer(1),
		"DATA\r\n",
		Text.GetBuffer(1),
		"QUIT\r\n",
		NULL
	};

	
	WSADATA	Wsa;
	
	WSAStartup(0x0101,&Wsa);
	SOCKET s = socket(AF_INET,SOCK_STREAM,0);

	SOCKADDR_IN	sin;
	sin.sin_addr.s_addr = inet_addr(m_sServer);
	sin.sin_family = AF_INET;
	sin.sin_port = htons(25);

	if(connect(s,(LPSOCKADDR)&sin,sizeof(sin)) == SOCKET_ERROR)
		MessageBox("Error connect to server :(","Error");


	int iLength = 0;
	int iEnd = 0;
	char sBuff[255] = "";
	int iMsg = 0;

	do
	{
		iLength = recv(s,(LPSTR)sBuff+iEnd, sizeof(sBuff)-iEnd,0);
		iEnd += iLength;
		sBuff[iEnd] = '\0';
		send(s,(LPSTR)MailMessage[iMsg],strlen(MailMessage[iMsg]),0);
		iMsg++;
		MessageBox(sBuff);
	}while(MailMessage[iMsg]);

	closesocket(s);
	WSACleanup();
	
}
