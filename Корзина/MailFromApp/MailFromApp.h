// MailFromApp.h : main header file for the MAILFROMAPP application
//

#if !defined(AFX_MAILFROMAPP_H__CC5AFD45_EFE7_49DD_AB4F_209EEE01849E__INCLUDED_)
#define AFX_MAILFROMAPP_H__CC5AFD45_EFE7_49DD_AB4F_209EEE01849E__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CMailFromAppApp:
// See MailFromApp.cpp for the implementation of this class
//

class CMailFromAppApp : public CWinApp
{
public:
	CMailFromAppApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMailFromAppApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CMailFromAppApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MAILFROMAPP_H__CC5AFD45_EFE7_49DD_AB4F_209EEE01849E__INCLUDED_)
