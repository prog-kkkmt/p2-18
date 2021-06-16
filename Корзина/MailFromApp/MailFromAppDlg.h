// MailFromAppDlg.h : header file
//

#if !defined(AFX_MAILFROMAPPDLG_H__59B358BA_DD91_4FD9_A9D3_D81D5CA71D04__INCLUDED_)
#define AFX_MAILFROMAPPDLG_H__59B358BA_DD91_4FD9_A9D3_D81D5CA71D04__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CMailFromAppDlg dialog

class CMailFromAppDlg : public CDialog
{
// Construction
public:
	CMailFromAppDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CMailFromAppDlg)
	enum { IDD = IDD_MAILFROMAPP_DIALOG };
	CString	m_sFrom;
	CString	m_sServer;
	CString	m_sText;
	CString	m_sTo;
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMailFromAppDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	//{{AFX_MSG(CMailFromAppDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnSend();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MAILFROMAPPDLG_H__59B358BA_DD91_4FD9_A9D3_D81D5CA71D04__INCLUDED_)
