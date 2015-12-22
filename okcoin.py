import sys
import argparse
import quickfix as fix
import quickfix44 as fix44
import my_api
import time

api_key=my_api.api_key
secret_key=my_api.secret_key

class Application(fix.Application):

    def onCreate(self, sessionID):
        self.sessionID = sessionID
        print "Application created - session: %s." % sessionID.toString()
        return

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        print "Successful Logon to session."

        # get session
        session = fix.Session.lookupSession(sessionID)

        # orderbook data request
        message = self.createOrderBookRequest()
        fix.Session.sendToTarget( message, sessionID ) # send message

        # live trade data request 
        message = self.createLiveTradesRequest()
        fix.Session.sendToTarget( message, sessionID ) # send message
 
        return

    def onLogout(self, sessionID): 
        print "Client logout or falied to login." 
        return

    def toAdmin(self, message, sessionID):
        username = fix.Username(api_key)
        password = fix.Password(secret_key) 
        message.setField(username);
	message.setField(password);

        #print "Sent the Admin following message: %s" % message.toString()
        return

    def fromAdmin(self, message, sessionID):
        print "Received the Admin following message: %s" % message.toString()
        return

    def toApp(self, message, sessionID):
        print "Sent the following message: %s" % message.toString()
        return

    def fromApp(self, message, sessionID):
        print "Received the following message: %s" % message.toString()
        return

    def run(self): 
        print 'Do whatever you want.'

    def createOrderBookRequest(self):
        orderBookRequest = fix44.MarketDataRequest()
        noRelatedSym = fix44.MarketDataRequest.NoRelatedSym()
        noRelatedSym.setField(fix.Symbol('BTC/CNY'))
	orderBookRequest.addGroup(noRelatedSym)

	orderBookRequest.setField(fix.MDReqID("123")) # Unique ID assigned to this request
	orderBookRequest.setField(fix.SubscriptionRequestType('1')) # 0 = Snapshot 
                                                                    # 1 = Snapshot + Subscribe 
                                                                    # 2 Unsubscribe
	orderBookRequest.setField(fix.MDUpdateType(1)) # 0 = full refresh, 1: incremental refresh
	orderBookRequest.setField(fix.MarketDepth(0))  # 0 = full book, 

	group1 = fix44.MarketDataRequest.NoMDEntryTypes()
	group1.setField(fix.MDEntryType('0')) # bids
	orderBookRequest.addGroup(group1)

	group2 = fix44.MarketDataRequest.NoMDEntryTypes()
	group2.setField(fix.MDEntryType('1')) # asks
	orderBookRequest.addGroup(group2)

        return orderBookRequest
	
    def createLiveTradesRequest(self): 
        liveTradesRequest = fix44.MarketDataRequest()
        noRelatedSym = fix44.MarketDataRequest.NoRelatedSym()
        noRelatedSym.setField(fix.Symbol("BTC/CNY"))
        liveTradesRequest.addGroup(noRelatedSym)

        liveTradesRequest.setField(fix.MDReqID("123"))
        liveTradesRequest.setField(fix.SubscriptionRequestType('1'))
        liveTradesRequest.setField(fix.MarketDepth(0))

        group = fix44.MarketDataRequest.NoMDEntryTypes()
        group.setField(fix.MDEntryType('2')) # trade
        liveTradesRequest.addGroup(group)

        return liveTradesRequest

def main(config_file):
    try:
        settings = fix.SessionSettings(config_file)
        print '1'
        application = Application()
        print '2'
        storeFactory = fix.FileStoreFactory(settings)
        print '3'
        logFactory = fix.FileLogFactory(settings)
        print '4'
        initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
        print '5'
        initiator.start()
        print '6'
        #application.run()
        time.sleep(300)
        print '7'
        initiator.stop()
        print '8'

    except (fix.ConfigError, fix.RuntimeError), e:
        print e

if __name__=='__main__':
    #parser = argparse.ArgumentParser(description='FIX Client')
    #parser.add_argument('file_name', type=str, help='Name of configuration file')
    #args = parser.parse_args()
    #main(args.file_name)

    main('okcoin.cfg')
