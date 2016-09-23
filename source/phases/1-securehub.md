ARPA2 phase 1: SecureHub
========================

>   *The SecureHub phase establishes a number of foundations for security.  In
>   spite of all the attention that has gone into our online security, much of
>   it does not really come together.*

This is the first phase of ARPA2, and it is targeted at delivering a number of
security premises on which the later phases can build.  The end-user appeal of
this layer is not very direct, but without this the IdentityHub phase would not
be possible.

The main projects in SecureHub are:

-   **TLS Pool** is a daemon that takes TLS out of applications.  The reasoning
    is that application developers have another mind set (namely, a functional
    drive) than security experts (who want to lock out anything dangerous) and
    that these are best handled in different bits of software.  The TLS Pool is
    a background program, with its own memory regions, in which it may juggle
    credentials without the application ever needing to worry about it.  The
    interface between TLS Pool and application talks of identities, in the form
    of a domain name or a user under a domain name; integration with the TLS
    Pool from an application’s perspective tends to take only an hour!

-   **SteamWorks** distributes configuration information over LDAP.  This means
    that central configuration (or, if you like the term, provisioning of
    configuration) is possible.  This is useful in many situations where users
    are less qualified to do so, and prefer to leave technical matters to a more
    qualified person, be it a company’s administrator or a security service
    provider.  Although SteamWorks makes it possible to centralise control, it
    still is a matter of subscription from the client’s end — and therefore, a
    choice made on the client machine.

-   **Kerberos** is a very old security protocol, but it is also the best option
    when dealing with centralised authentication.  So, if you are to centrally
    manage accounts for users, groups and roles, as well as secure connections
    to services and machines, then Kerberos is ideal.  This is the customary
    choice in companies of any reasonable scale (they might call it Active
    Directory, Samba, FreeIPA or Windows for Workgroups — but that still means
    they use Kerberos for authentication).  In the IdentityHub phase, we will
    turn to extensions that make Kerberos suitable as a mechanism for the
    Internet as a whole and for card-swipe usage patterns; but in the SecureHub
    phase, our aim is to use it locally, under our own domain or realm.

-   **TLS-KDH** introduces Kerberos in TLS.  We do this in a modern way, where
    we always incorporate the mechanisms for Forward Secrecy.  The integration
    of Kerberos with HTTP or HTTPS is surprisingly weak, even if it is in high
    demand.  Adding a strong Kerberos mechanism to TLS means that we can use it
    in HTTPS, but also for STARTTLS-styled protocols like mail, chat and
    telephony — the list of uses is virtually endless.  Given that the call for
    TLS is resounding these days, and given the inefficiency of doing this with
    X.509 certificates, it is good to know that our research has shown that
    authentication with TLS-KDH is about 5000 times as efficient as when using
    X.509 certificates.

After the SecureHub project, it is our hope to see a lot of spin-off work.  It
should not surprise anyone that TLS-KDH is integrated into the TLS Pool, so any
application using that has a great opportunity of hooking into the InternetWide
Architecture.

Proper integration of the TLS Pool does not only mean adding a generic TLS
tunnel around it (though one is delivered with the TLS Pool), because that
leaves the problem of communicating the authenticated identities of the two
sides to the wrapped program.  The best integration comes from a client program,
be it a web server or client or proxy, or perhaps mail tools.  When these start
to communicate TLS, they may hand off their socket to the TLS Pool, indicate
what is being expected about identities and tell the TLS Pool to start shaking
hands with the other side.  When done, the TLS Pool should respond with the
authenticated identities of the local and remote end, or none if they could not
be authenticated.  The program then continues over a new socket, speaking the
plaintext version of the protocol but resting assured that an external daemon
handles connection privacy and integrity in just the way the user likes to have
that handled.  The authenticated identities can henceforth be used in the
application program.

This use of the TLS Pool means that TLS-KDH can be used where it is supported —
a great gain in efficiency, and proponents of short-lived credentials might
argue that the security is also under much tighter control.  Future extensions
to Kerberos, such as realm crossover and pseudonymity will all be handled
automatically.  And when the IdentiyHub starts supporting centralised creation
of new identities, the TLS Pool will follow suit — and the application can
safely ignore any such thing.

We even intend to extend the TLS Pool idea at some point, to incorporate
alternatives to TLS, such as SSH and GSS-API based protocols.  This would lead
to a slightly modified flow in applications, but only during their call for a
handshake — after that they would once more have authenticated identities on
each end, and reliance on another program to handle privacy and authenticity.
This could give rise to alternative protocol elements such as `STARTSSH` and
`STARTGSS` — thereby allowing us to switch from TLS to another security protocol
if we feel so inclined.  In security, it is always good to have one to throw
away, just to help us instantly resolve security problems when the need arises.
