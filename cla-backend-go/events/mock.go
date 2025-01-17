// Copyright The Linux Foundation and each contributor to CommunityBridge.
// SPDX-License-Identifier: MIT
//

// Code generated by MockGen. DO NOT EDIT.
// Source: github.com/communitybridge/easycla/cla-backend-go/events (interfaces: Service)

// Package events is a generated GoMock package.
package events

import (
	context "context"
	reflect "reflect"

	models "github.com/communitybridge/easycla/cla-backend-go/gen/models"
	events0 "github.com/communitybridge/easycla/cla-backend-go/gen/restapi/operations/events"
	gomock "github.com/golang/mock/gomock"
)

// MockService is a mock of Service interface
type MockService struct {
	ctrl     *gomock.Controller
	recorder *MockServiceMockRecorder
}

// MockServiceMockRecorder is the mock recorder for MockService
type MockServiceMockRecorder struct {
	mock *MockService
}

// NewMockService creates a new mock instance
func NewMockService(ctrl *gomock.Controller) *MockService {
	mock := &MockService{ctrl: ctrl}
	mock.recorder = &MockServiceMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use
func (m *MockService) EXPECT() *MockServiceMockRecorder {
	return m.recorder
}

// GetClaGroupEvents mocks base method
func (m *MockService) GetClaGroupEvents(arg0 string, arg1 *string, arg2 *int64, arg3 bool, arg4 *string) (*models.EventList, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetClaGroupEvents", arg0, arg1, arg2, arg3, arg4)
	ret0, _ := ret[0].(*models.EventList)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetClaGroupEvents indicates an expected call of GetClaGroupEvents
func (mr *MockServiceMockRecorder) GetClaGroupEvents(arg0, arg1, arg2, arg3, arg4 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetClaGroupEvents", reflect.TypeOf((*MockService)(nil).GetClaGroupEvents), arg0, arg1, arg2, arg3, arg4)
}

// GetCompanyClaGroupEvents mocks base method
func (m *MockService) GetCompanyClaGroupEvents(arg0, arg1, arg2 string, arg3 *string, arg4 *int64, arg5 bool) (*models.EventList, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetCompanyClaGroupEvents", arg0, arg1, arg2, arg3, arg4, arg5)
	ret0, _ := ret[0].(*models.EventList)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetCompanyClaGroupEvents indicates an expected call of GetCompanyClaGroupEvents
func (mr *MockServiceMockRecorder) GetCompanyClaGroupEvents(arg0, arg1, arg2, arg3, arg4, arg5 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetCompanyClaGroupEvents", reflect.TypeOf((*MockService)(nil).GetCompanyClaGroupEvents), arg0, arg1, arg2, arg3, arg4, arg5)
}

// GetCompanyEvents mocks base method
func (m *MockService) GetCompanyEvents(arg0, arg1 string, arg2 *string, arg3 *int64, arg4 bool) (*models.EventList, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetCompanyEvents", arg0, arg1, arg2, arg3, arg4)
	ret0, _ := ret[0].(*models.EventList)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetCompanyEvents indicates an expected call of GetCompanyEvents
func (mr *MockServiceMockRecorder) GetCompanyEvents(arg0, arg1, arg2, arg3, arg4 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetCompanyEvents", reflect.TypeOf((*MockService)(nil).GetCompanyEvents), arg0, arg1, arg2, arg3, arg4)
}

// GetCompanyFoundationEvents mocks base method
func (m *MockService) GetCompanyFoundationEvents(arg0, arg1, arg2 string, arg3 *string, arg4 *int64, arg5 bool) (*models.EventList, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetCompanyFoundationEvents", arg0, arg1, arg2, arg3, arg4, arg5)
	ret0, _ := ret[0].(*models.EventList)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetCompanyFoundationEvents indicates an expected call of GetCompanyFoundationEvents
func (mr *MockServiceMockRecorder) GetCompanyFoundationEvents(arg0, arg1, arg2, arg3, arg4, arg5 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetCompanyFoundationEvents", reflect.TypeOf((*MockService)(nil).GetCompanyFoundationEvents), arg0, arg1, arg2, arg3, arg4, arg5)
}

// GetFoundationEvents mocks base method
func (m *MockService) GetFoundationEvents(arg0 string, arg1 *string, arg2 *int64, arg3 bool, arg4 *string) (*models.EventList, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetFoundationEvents", arg0, arg1, arg2, arg3, arg4)
	ret0, _ := ret[0].(*models.EventList)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetFoundationEvents indicates an expected call of GetFoundationEvents
func (mr *MockServiceMockRecorder) GetFoundationEvents(arg0, arg1, arg2, arg3, arg4 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetFoundationEvents", reflect.TypeOf((*MockService)(nil).GetFoundationEvents), arg0, arg1, arg2, arg3, arg4)
}

// GetRecentEvents mocks base method
func (m *MockService) GetRecentEvents(arg0 *int64) (*models.EventList, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "GetRecentEvents", arg0)
	ret0, _ := ret[0].(*models.EventList)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetRecentEvents indicates an expected call of GetRecentEvents
func (mr *MockServiceMockRecorder) GetRecentEvents(arg0 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetRecentEvents", reflect.TypeOf((*MockService)(nil).GetRecentEvents), arg0)
}

// LogEvent mocks base method
func (m *MockService) LogEvent(arg0 *LogEventArgs) {
	m.ctrl.T.Helper()
	m.ctrl.Call(m, "LogEvent", arg0)
}

// LogEvent indicates an expected call of LogEvent
func (mr *MockServiceMockRecorder) LogEvent(arg0 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "LogEvent", reflect.TypeOf((*MockService)(nil).LogEvent), arg0)
}

// LogEventWithContext mocks base method
func (m *MockService) LogEventWithContext(arg0 context.Context, arg1 *LogEventArgs) {
	m.ctrl.T.Helper()
	m.ctrl.Call(m, "LogEventWithContext", arg0, arg1)
}

// LogEventWithContext indicates an expected call of LogEventWithContext
func (mr *MockServiceMockRecorder) LogEventWithContext(arg0, arg1 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "LogEventWithContext", reflect.TypeOf((*MockService)(nil).LogEventWithContext), arg0, arg1)
}

// SearchEvents mocks base method
func (m *MockService) SearchEvents(arg0 *events0.SearchEventsParams) (*models.EventList, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "SearchEvents", arg0)
	ret0, _ := ret[0].(*models.EventList)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// SearchEvents indicates an expected call of SearchEvents
func (mr *MockServiceMockRecorder) SearchEvents(arg0 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "SearchEvents", reflect.TypeOf((*MockService)(nil).SearchEvents), arg0)
}
