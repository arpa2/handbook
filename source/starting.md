Getting Started
---------------

>   *How can you get on board?  What are the steps to gradually incorporate the
>   ARPA2 projects, and by that the InternetWide Architecture, into your
>   systems?*

This chapter describes how you can get on board, and start to use the components
that we built for this ever-expanding software stack.  We do not target specific
use cases yet.  The steps described below are global, and reference more
detailed instructions (or indicate that this software is still being worked on).

### Adopting PKCS \#11 (standardised secret store)

In case you haven’t heard of PKCS \#11, it is an API that is designed to conceal
secret and private keys from being observed, or exported in plain view.  These
objects are the cornerstones of cryptographic protection, and being unable to
replicate them is helpful to your security and privacy.

>   **Status:** There is a wide array of mature software choices for PKCS \#11,
>   ranging from software, through simple USB keys, to high-end, hardened
>   bastions that would rather destroy your keys than release them to a physical
>   intruder.

-   PKCS \#11 is a foundation on which we built the TLS Pool.  We realise it is
    an extra effort to install and get used to, but PKCS \#11 adds great value
    in terms of flexible security deployments.  Once it is setup and running, it
    should not give any more headaches, other than to attackers after your keys.

-   We advise you to get started with SoftHSMv2, because it is a sophisticated
    and mature open source product.  If the need for hardware protection arises
    later on, you merely swap the library that implements your PKCS \#11 API
    (and juggle keys as deemed necessary).

-   If you want to “play” with PKCS \#11, you may have a look at your mail or
    web clients; they often support plugging in PKCS \#11 libraries, on which
    you can then store your local key material and certificates.  This is also
    what the TLS Pool does; it stores private keys behind a PKCS \#11 API and
    links them to certificates that are stored in a local identity database.

-   There is a standard for [pkcs11: URIs](https://tools.ietf.org/html/rfc7512)
    which can describe either tokens or objects (such as keys, certificates, or
    data) on that token.  This is not a *location* but an *identifier*, in the
    sense that it provides selection criteria for a token and, given extra
    parameters, objects on a token.  You will need to supply your software with
    a library that implements the PKCS \#11 API along with each URI.

-   When you get started with the TLS Pool, we will talk you through the steps
    of using PKCS \#11 for that purpose.  These steps will assume SoftHSMv2 and
    GnuTLS tooling, but you can easily vary if you feel a need; PKCS \#11
    solutions are fairly exchangeable, other than that their implemented
    security level varies drastically.

-   When we initiate the IdentityHub, we are going to manage PKCS \#11 at a
    (paid to be trustworthy) hosting provider — or perhaps on your Raspberry Pi
    at home — and we will then introduce Remote PKCS \#11.  This will allow you
    to share your identities anywhere you are, including on your mobile device.
    And yes, we have concerned ourselves with the security of that design!

### Adopting TLS Pool (splitting security from applications)

The TLS Pool is the piece of software that takes security knowledge out of
applications.  It relies on PKCS \#11 and, in part because of that, is not easy
to get started.  Once it is running however, you should find that it easily
“clicks in” and grants you a lot of control over security, in one place for all
the applications concerned.  As a matter of fact, you can even centralise
management.

>   **Status:** The TLS Pool works well on servers, but using it on client
>   platforms is a bit awkward.  This is mostly due to lacking [multi-user
>   support](https://github.com/arpa2/tlspool/issues/36), but if your client is
>   in practice a single-user platform you should be able to use the TLS Pool
>   quite nicely.

-   The first thing to do is perhaps to start using the TLS Pool, and use it
    from the applications that you rely on.

-   If your server does not rely on authenticated client identities, than it may
    suffice to simply use the TLS Tunnel distributed with the TLS Pool.  This
    tool can even use simple scripts to talk a remote server into `STARTTLS`
    mode, and then proceed as before.

-   If your client wants to use the TLS Pool to authenticate to a server, it may
    also suffice to use the TLS Tunnel.  It will authenticate the client, so
    this may even add value to non-TLS applications.  For instance, you could
    direct your mail client to a locally hosted SMTP server, which is then
    redirected by the TLS Tunnel, authenticating with `STARTTLS` and using
    credentials kept in the TLS Pool.  Dependent on the server side, this may be
    helpful or confusing to client authentication; the ideal situation being to
    rely on `SASL EXTERNAL` authentication, referring back to an identity that
    was authenticated over TLS.

-   Use of the TLS Pool for authentaction by applications is not something that
    the ARPA2 project can directly influence, but it may help if you ask the
    producers of your favourite pieces of software to look into it — or if you
    organise the needed patches.  It has been shown repeatedly that the addition
    of the TLS Pool to an existing application takes about an hour for someone
    well-versed in the application’s inner structure!

-   If you have an application that has “add TLS” on the TODO list, think no
    longer — adopt the TLS Pool.  It will save you a lot of anxiety about
    security configuration, where to load certificates from and how to handle
    the accompanying private keys in a secure manner.  All this is delegated to
    the TLS Pool.  In fact, it will implement many more things than you would
    ever be likely to add — and you get it all for free.

### Adopting SteamWorks (LDAP configuration dissemination)

The idea of SteamWorks is to offer you with a configuration backbone.

>   **Status:** At this point, SteamWorks is in its infancy.  A few test setups
>   have shown to work though.

-   SteamWorks is founded on LDAP, for which we hope to simplify management
    through a front-end that takes care of the intricacies of running a complex
    daemon.  SteamWorks uses LDAP SyncRepl as a subscription mechanism for
    near-instant dissemination of configuration changes to those clients that
    have subscribed.  The design of SteamWorks incorporates components that help
    to isolate networks from connectivity problems to remote parts of the
    Internet.

-   SteamWorks delivers configuration information to backends, using
    configuration scripts to determine what information should be taken from
    where in LDAP, and how to pass it on to those backends.  The backends will
    then store the information in a form suitable for the targeted software
    system.

-   As a first example, the TLS Pool has a backend for SteamWorks, permitting
    the complexities of TLS configuration to be made centrally, for instance by
    an administrator.  This releases individual users from the concerns that
    come with the specialised domain of security.  As soon as a security problem
    pops up, a change can be made in the SteamWorks configuration and subscribed
    clients would virtually immediately pickup the change and process it
    locally, is the underlying idea.

### Adopting Kerberos (or await IdentiyHub)

We advise you to start using Kerberos as your central authentication mechanism.

>   **Status:** Kerberos is very robust, very secure and very well integrated
>   into software.  Setting it up is not always easy, but once setup life
>   simplifies to a single-signon system.  Note that the one weak point at this
>   time is support for HTTPS — and that we are working on resolving that
>   generically, by adding Kerberos to TLS in the form of TLS-KDH.

-   Kerberos offers “single sign-on”, which means that you login once (usually
    at the start of the day) and continue to use the initial credential received
    for hours to go.  You need to do no further logins, as any new service
    ticket needed during those hours are derived from your initial start-of-day
    credential.  On top of that, Kerberos is very fast, because it is built on
    symmetric-key algorithms such as AES-256.

-   Kerberos is integrated into many protocols, including SMTP, IMAP, LDAP and
    SSH.  You will be pleasantly surprised by how much faster your SSH logins
    will be with Kerberos, compared to using the SSH Agent or mundane/manual
    password entry.

-   Be aware that we will offer Kerberos as part of the upcoming project phase,
    IdentityHub.  This means that you should think ahead if you want to setup a
    quick test platform to cover the time until we get there, or that you prefer
    to wait a while.  Be advised that setting up the KDC is the most difficult
    part of running Kerberos, which is why we will “web-wrap” it for less
    technical domain owners, but a straightforward setup on a single node is
    quite doable for an experienced administrator.

-   Be advised that the IdentityHub works towards automated realm crossover
    between Kerberos realms, in a way that allows clients of on realm to
    authenticate to another, even if they had not been introduced before.  The
    technique for doing so will likely derive its security from DANE.  Note that
    authentication does not imply authorisation: you may be able to prove to
    anyone who you are, but the question remains if you are welcome to use any
    given service.

### Adopt RADIUS or Diameter (for authorisation)

The RADIUS system and its follow-up Diameter are widely used to centralise
authentication, authorisation and accounting within a domain, or secure realm.
Although authentication (who is it?) and authorisation (what may he do?) tend to
blur in these systems, they will answer questions like *Can Jack access the
files of Joe?* with *Yeah* or *Nay*.

>   **Status:** RADIUS is very stable, and in principle, so is Diameter.  The
>   latter is less often used, but has a few clever extensions.  When we come to
>   the ServiceHub, we will standardise on Diameter.  Mature systems exist to
>   connect RADIUS and Diameter, so that should not constrain your local choice.
>   New systems should probably consider Diameter, and break with the somewhat
>   overdue tradition of RADIUS.

-   As part of IdentityHub, we will support a flexible authorisation framework.
    It is assumed that a user’s identity is authenticated, and that its access
    to a resource is questioned.  A few examples are:

    -   Can this [user](http://donai.arpa2.net) act on behalf of that [user,
        group, role, alias or
        pseudonym](http://internetwide.org/blog/2015/04/23/id-3-idforms.html)?

    -   Is this [user](http://donai.arpa2.net) acceptable to the [access control
        list](http://donai.arpa2.net/acl.html) for the given
        [service](http://donai.arpa2.net/selector.html)?

-   We have not standardised the method of asking these questions yet.  This is
    in part due to our desire to retain privacy as much as we can; when we setup
    the SecureHub, we would prefer to not spread all information to each
    service, but hopefully answer little more than these direct questions in a
    way that they can easily cache.  And of course that also introduces concerns
    of efficiency of any such caches and the expediency of updates to them.

### Adopt modern Internet standards (in general)

In our work, we are going to make a few radical assumptions about support for
modern Internet protocol.  Some things simply cannot be done well on IPv4
(thanks to NAT traversal nightmares) and some things are simply not secure
without mechanisms like DNSSEC.

>   **Status:** Most of these technologies have been around for quite a while,
>   and their software has been well tested.  You may find that you are still an
>   early adopter, although you would also be surprised how well the uptake of
>   various modern developments has been in practice.

-   Adopt IPv6.  Really, when it comes to end-to-end communication you do not
    want to be dealing with NAT traversal issues.  Ask any self-acclaimed SIP
    expert about their fondness of NAT and they will show you their best
    daunting-nightmare grinn.  We are going to *require* IPv6 on various parts
    of our design, simply because it evades problems that are now in the way of
    progress, and because the inherent complexities of NAT traversal lead to
    complex code, complex networking problems and poor end-user experiences.

-   Adopt DNSSEC.  Start signing your zones, and validate your DNS queries.  We
    will *require* DNSSEC for a number of follow-up projects, for example to
    validate DANE entries, and perhaps SSHKEY records in DNS.  With DNSSEC in
    place, the DNS is a reliable database of domain-specific information;
    without DNSSEC, it cannot be used as a foundation for *anything* that is at
    risk of being abused.

-   Adopt SCTP.  This protocol sits next to UDP and TCP, and can actually behave
    like either.  In addition, it can run multiple streams at the same time.
    Particularly interesting is its support of a reliable, but not necessarily
    in-order delivery of frames, which happens to be very useful for systems
    that run on UDP to avoid head-of-line blockage but that need to resend at
    the application level to achieve a reliable service.  We will *require* SCTP
    for several of our services, among others for the ServiceHub project where
    it will be used as a sort of *umbilical cord* between hosting providers.
    Chances are that SIP infrastructure will also require SCTP, in support of
    longer messages that can then include security information.

-   Be advised that the IdentityHub and ServiceHub will export DANE records for
    services.  Research by SURFnet had led to the conclusion that the spread
    administration of DNS, certificates and servers makes DANE a potentially
    fragile system, but automation can be helpful to overcome that.

### Embrace for more...

The InternetWide Architecture encompasses much more.  As this project advances,
we will update this page with more steps that you can take.
